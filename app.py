import streamlit as st

st.title("APP CHO VAY ONLINE KHÁCH HÀNG CÁ NHÂN_ĐỀ TÀI 4_NGUYỄN HUỲNH NGỌC HÀ")

# Nhập dữ liệu
STV = st.number_input(
    "Nhập số tiền muốn vay (triệu đồng)",
    min_value=0.0,
    step=1.0
)

TGV = st.number_input(
    "Nhập thời gian vay (số năm)",
    min_value=0.0,
    step=1.0
)

LSV = st.number_input(
    "Nhập lãi suất cho vay (số thập phân, ví dụ 0.12)",
    min_value=0.0,
    step=0.01,
    format="%.4f"
)

TN = st.number_input(
    "Nhập thu nhập hàng tháng (triệu đồng)",
    min_value=0.0,
    step=1.0
)

SNTGD = st.number_input(
    "Nhập số người trong gia đình",
    min_value=0,
    step=1
)

PTMC = st.number_input(
    "Nhập số tiền phải trả cho khoản vay cũ (triệu đồng)",
    min_value=0.0,
    step=1.0
)

GTTSDB = st.number_input(
    "Nhập giá trị tài sản đảm bảo (triệu đồng)",
    min_value=0.0,
    step=1.0
)

STKH = st.number_input(
    "Nhập số tuổi của khách hàng",
    min_value=0,
    step=1
)

# Hằng số
CPSH = 5

# Nút tính toán
if st.button("Đánh giá khoản vay"):
    try:
        PTMM = (STV / (TGV * 12)) + (STV * (LSV / 12))
        DTI = (PTMC + PTMM) / (TN - SNTGD * CPSH)
        LTV = STV / GTTSDB

        st.write(f"**Chỉ số DTI:** {DTI * 100:.2f}%")
        st.write(f"**Chỉ số LTV:** {LTV * 100:.2f}%")

        if DTI <= 0.7 and LTV <= 0.7 and 18 <= STKH < 70:
            st.success("✅ ĐƯỢC CHO VAY")
        else:
            st.error("❌ KHÔNG ĐƯỢC CHO VAY")

    except ZeroDivisionError:
        st.warning("Vui lòng kiểm tra lại thời gian vay, thu nhập hoặc giá trị tài sản đảm bảo không được bằng 0.")
