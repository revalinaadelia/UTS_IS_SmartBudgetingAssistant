# ======================================================================
# Smart Budgeting Assistant (Forward & Backward Chaining)
# Anggota Kelompok NPC:
# 1. Betrand Daffarel (4523210029)
# 2. Eka Lidya Rahmadini (4523210039)
# 3. Revalina Adelia (4523210091) 
# ======================================================================

import streamlit as st
import pandas as pd

# ======================================================================
# KONFIGURASI HALAMAN
# ======================================================================
st.set_page_config(page_title="Smart Budgeting Assistant", page_icon="", layout="centered")
st.title("Smart Budgeting Assistant")
st.write("Atur keuangan kamu secara cerdas menggunakan sistem pakar berbasis **Forward** dan **Backward Chaining**.")

# ======================================================================
# UTILITY FUNCTIONS
# ======================================================================
def standardize_knowledge_base(facts, rules):
    """Mengubah semua fakta dan aturan menjadi huruf kecil untuk konsistensi."""
    standardized_facts = {f.lower() for f in facts}
    standardized_rules = [({p.lower() for p in premise}, conclusion.lower()) for premise, conclusion in rules]
    return standardized_facts, standardized_rules

def forward_chaining(facts, rules, verbose=False):
    """Melakukan penalaran maju (forward chaining)."""
    facts = set(facts)
    trace = []
    iteration = 0
    changed = True

    while changed:
        iteration += 1
        changed = False
        if verbose:
            trace.append(f"Iterasi {iteration} | Fakta saat ini: {sorted(facts)}")
        for premise, conclusion in rules:
            if premise.issubset(facts) and conclusion not in facts:
                facts.add(conclusion)
                changed = True
                trace.append(f"✓ Aturan diterapkan: {set(premise)} → {conclusion}")
        if verbose and not changed:
            trace.append("Tidak ada aturan lain yang dapat diterapkan.")
    return facts, trace

def index_rules_by_conclusion(rules):
    """Membuat indeks aturan berdasarkan kesimpulan untuk proses backward chaining."""
    index = {}
    for premise, conclusion in rules:
        index.setdefault(conclusion, []).append(premise)
    return index

def backward_chaining(goal, facts, rule_index, visited=None, depth=0):
    """Melakukan penalaran mundur (backward chaining)."""
    indent = "  " * depth
    if visited is None:
        visited = set()
    trace = [f"{indent}Periksa tujuan: {goal}"]

    if goal in facts:
        trace.append(f"{indent}✔ Tujuan '{goal}' sudah ada di fakta.")
        return True, trace

    if goal in visited:
        trace.append(f"{indent}✗ Terjadi loop pada '{goal}'.")
        return False, trace
    visited.add(goal)

    if goal not in rule_index:
        trace.append(f"{indent}✗ Tidak ada aturan yang menyimpulkan '{goal}'.")
        return False, trace

    for premise_set in rule_index[goal]:
        trace.append(f"{indent}Coba aturan: {set(premise_set)} → {goal}")
        all_ok = True
        subtrace = []
        for p in premise_set:
            ok, sub = backward_chaining(p, facts, rule_index, visited, depth + 1)
            subtrace.extend(sub)
            if not ok:
                all_ok = False
                trace.append(f"{indent}  ✗ Premis '{p}' gagal dibuktikan.")
                break
        trace.extend(subtrace)
        if all_ok:
            trace.append(f"{indent}✔ Tujuan '{goal}' berhasil dibuktikan melalui {set(premise_set)}.")
            return True, trace

    trace.append(f"{indent}✗ Semua aturan untuk '{goal}' gagal dibuktikan.")
    return False, trace

# ======================================================================
# INPUT DATA PENGGUNA
# ======================================================================
st.header("Input Data Keuangan")
income = st.number_input("Masukkan pendapatan bulanan kamu (Rp)", min_value=0, step=500000, format="%d")

st.divider()
st.subheader("Masukkan Daftar Pengeluaran Bulanan Kamu")

if "expenses" not in st.session_state:
    st.session_state.expenses = []

with st.form("add_expense", clear_on_submit=True):
    col1, col2 = st.columns([2, 1])
    with col1:
        expense_name = st.text_input("Nama Pengeluaran (contoh: Makan, Transportasi, Hiburan, dll.)")
    with col2:
        expense_amount = st.number_input("Jumlah (Rp)", min_value=0, step=50000, format="%d")
    add = st.form_submit_button("Tambah Pengeluaran")

    if add:
        if expense_name and expense_amount > 0:
            st.session_state.expenses.append({"Nama": expense_name, "Jumlah": expense_amount})
            st.success(f"Pengeluaran '{expense_name}' berhasil ditambahkan!")
        else:
            st.warning("Isi nama dan nominal pengeluaran dengan benar.")

if len(st.session_state.expenses) > 0:
    df = pd.DataFrame(st.session_state.expenses)
    st.dataframe(df, hide_index=True)
    total_expense = int(df["Jumlah"].sum())
    st.info(f"**Total pengeluaran:** Rp {total_expense:,.0f}")
else:
    total_expense = 0
    st.warning("Belum ada pengeluaran yang dimasukkan.")

st.divider()

# ======================================================================
# PILIHAN RENCANA KEUANGAN
# ======================================================================
st.subheader("Pilih Rencana Keuangan Kamu")
invest = st.checkbox("Investasi")
saving = st.checkbox("Tabungan")
emergency = st.checkbox("Dana Darurat")

percentages = {}
if invest:
    percentages["Investasi"] = st.number_input("Persentase Investasi (%) (disarankan 50%)", 0, 100, 50, 5)
if saving:
    percentages["Tabungan"] = st.number_input("Persentase Tabungan (%) (disarankan 30%)", 0, 100, 30, 5)
if emergency:
    percentages["Dana Darurat"] = st.number_input("Persentase Dana Darurat (%) (disarankan 20%)", 0, 100, 20, 5)

st.divider()

# ======================================================================
# SETUP (FAKTA DAN ATURAN)
# ======================================================================
st.header("Setup (Fakta dan Aturan)")

# Fakta awal akan dihasilkan otomatis dari input pengguna.
initial_facts_raw = set()

# Aturan Forward Chaining (Premis → Kesimpulan)
rules_raw = [
    # --- LEVEL 1: Kategori Pendapatan dan Pengeluaran ---
    # Jika pendapatan tinggi dan pengeluaran rendah, sistem menyarankan investasi agresif.
    ({"high_income", "low_expense"}, "rekomendasi_investasi_agresif"),

    # Jika pendapatan sedang dan pengeluaran tinggi, sistem menyarankan fokus pada tabungan stabil.
    ({"medium_income", "high_expense"}, "rekomendasi_tabungan_stabil"),

    # Jika pendapatan rendah dan pengeluaran sangat tinggi, sistem menyarankan pemangkasan biaya.
    ({"low_income", "very_high_expense"}, "rekomendasi_pangkas_biaya"),

    # --- LEVEL 2: Analisis Sisa Uang ---
    # Jika sisa uang besar, sistem menyarankan meningkatkan alokasi investasi/tabungan.
    ({"large_remaining"}, "saran_tambah_alokasi"),

    # Jika sisa uang sangat kecil, sistem memberi peringatan potensi kekurangan kas.
    ({"small_remaining"}, "peringatan_sisa_kecil"),

    # --- LEVEL 3: Evaluasi Persentase Alokasi ---
    # Jika persentase investasi kurang dari batas ideal, sistem menyarankan menambah investasi.
    ({"low_investment_allocation"}, "saran_tambah_investasi"),

    # Jika persentase tabungan terlalu kecil, sistem menyarankan meningkatkan tabungan.
    ({"low_saving_allocation"}, "saran_tambah_tabungan"),

    # Jika dana darurat tidak mencukupi, sistem menyarankan menambah alokasi dana darurat.
    ({"low_emergency_allocation"}, "saran_tambah_dana_darurat"),

    # --- LEVEL 4: Peringatan Tambahan ---
    # Jika pengeluaran sangat tinggi, sistem memberi peringatan untuk dikurangi.
    ({"very_high_expense"}, "peringatan_kurangi_pengeluaran"),

    # Jika pengeluaran rendah dengan pendapatan sedang, sistem merekomendasikan rencana keuangan moderat.
    ({"low_expense", "medium_income"}, "rekomendasi_moderat"),
]

st.code(f"Jumlah aturan dalam basis pengetahuan: {len(rules_raw)}", language="python")

# ======================================================================
# FUNGSI PEMBENTUK FAKTA DARI INPUT
# ======================================================================
def derive_initial_facts(income, total_expense, percentages):
    facts = set()

    # Klasifikasi pendapatan
    if income >= 15000000:
        facts.add("high_income")
    elif income >= 6000000:
        facts.add("medium_income")
    else:
        facts.add("low_income")

    # Rasio pengeluaran
    if income > 0:
        ratio = total_expense / income
    else:
        ratio = 0
    if ratio > 0.7:
        facts.add("very_high_expense")
    elif ratio >= 0.5:
        facts.add("high_expense")
    elif ratio < 0.3:
        facts.add("low_expense")

    # Fakta tentang sisa uang
    remaining = income - total_expense
    if remaining < 0.05 * income:
        facts.add("small_remaining")
    elif remaining >= 0.2 * income:
        facts.add("large_remaining")

    # Fakta tentang alokasi persentase
    if "Investasi" in percentages and percentages["Investasi"] < 50:
        facts.add("low_investment_allocation")
    if "Tabungan" in percentages and percentages["Tabungan"] < 30:
        facts.add("low_saving_allocation")
    if "Dana Darurat" in percentages and percentages["Dana Darurat"] < 20:
        facts.add("low_emergency_allocation")

    return facts, remaining

# ======================================================================
# PROSES INFERENSI (FORWARD & BACKWARD)
# ======================================================================
if st.button("Jalankan Inferensi"):
    if income == 0:
        st.warning("Masukkan pendapatan terlebih dahulu!")
    elif total_expense == 0:
        st.warning("Masukkan data pengeluaran terlebih dahulu!")
    else:
        initial_facts, remaining = derive_initial_facts(income, total_expense, percentages)
        initial_facts, rules = standardize_knowledge_base(initial_facts, rules_raw)

        final_facts, forward_trace = forward_chaining(initial_facts, rules, verbose=True)

        st.write(f"**Sisa uang setelah pengeluaran:** Rp {remaining:,.0f}")

        if remaining <= 0:
            st.error("Pengeluaran kamu melebihi atau sama dengan pendapatan. Kurangi pengeluaran terlebih dahulu.")
        else:
            st.success("Perhitungan selesai. Sistem pakar berhasil melakukan inferensi.")

            # -------------------------------
            # Hasil Forward Chaining
            # -------------------------------
            st.divider()
            st.subheader("Hasil Inferensi (Forward Chaining)")
            st.write(f"- Fakta awal: {sorted(initial_facts)}")
            st.write(f"- Fakta tambahan (hasil inferensi): {sorted(final_facts - initial_facts)}")

            with st.expander("Lihat jejak forward chaining (trace)"):
                for line in forward_trace:
                    st.text(line)

            # -------------------------------
            # Hasil Backward Chaining
            # -------------------------------
            st.divider()
            st.subheader("Verifikasi Otomatis (Backward Chaining)")
            rule_index = index_rules_by_conclusion(rules)

            new_conclusions = sorted([f for f in final_facts if f not in initial_facts])
            if not new_conclusions:
                st.warning("Tidak ada kesimpulan baru untuk diverifikasi.")
            else:
                for goal in new_conclusions:
                    st.markdown(f"**Menguji tujuan:** `{goal}`")
                    ok, backward_trace = backward_chaining(goal, final_facts, rule_index)
                    if ok:
                        st.success(f"Tujuan '{goal}' berhasil dibuktikan!")
                    else:
                        st.error(f"Tujuan '{goal}' tidak dapat dibuktikan.")
                    with st.expander(f"Lihat jejak pembuktian untuk '{goal}'"):
                        for j in backward_trace:
                            st.text(j)

st.caption("Dibuat oleh Kelompok NPC — Sistem Pakar Smart Budgeting (Forward & Backward Chaining)")