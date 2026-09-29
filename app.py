import streamlit as st
from datetime import date, datetime, timezone, timedelta
from calendar import monthrange
from collections import defaultdict
import pandas as pd
from pathlib import Path as FilePath
import uuid
import json
import re
import html as html_lib
import streamlit.components.v1 as components

try:
    from supabase import create_client
except ImportError:
    create_client = None

st.set_page_config(
    page_title="Đặt Cơm Online",
    page_icon="🍱",
    layout="wide"
)

# ============================================================
# GIỮ THANH MENU TAB Ở TRÊN KHI CUỘN TRANG
# ============================================================
st.markdown("""
<style>
/* ===== GIỮ CẢ TIÊU ĐỀ + MENU KHI CUỘN ===== */

/* Khối tiêu đề ứng dụng luôn đứng ở trên */
.sticky-app-header {
    position: sticky;
    top: 0;
    z-index: 1002;
    background: white;
    padding: 0.55rem 0 0.8rem 0;
    border-bottom: 1px solid #f1f1f1;
}

.sticky-app-header .app-title {
    font-size: 2.35rem;
    font-weight: 800;
    line-height: 1.15;
    color: #1f2a44;
}

.sticky-app-header .app-subtitle {
    margin-top: 0.55rem;
    font-size: 0.96rem;
    color: #8a8f98;
}

/* Thanh tab bám ngay dưới tiêu đề */
div[data-testid="stTabs"] > div[data-baseweb="tab-list"] {
    position: sticky;
    top: 92px;
    z-index: 1001;
    background: white;
    padding-top: 0.3rem;
    border-bottom: 1px solid #e5e7eb;
}

/* Cho phép sticky hoạt động đúng trong vùng tabs */
div[data-testid="stTabs"] {
    overflow: visible !important;
}

/* Giảm khoảng trống khi menu đang sticky */
div[data-baseweb="tab-list"] {
    backdrop-filter: blur(8px);
}

/* ===== THANH MENU CHÍNH NỔI BẬT ===== */
div[data-baseweb="tab-list"] {
    gap: 0.7rem !important;
    padding: 0.55rem 0.25rem 0.65rem 0.25rem !important;
    background: #ffffff !important;
}

/* Từng tab giống nút điều hướng */
button[data-baseweb="tab"] {
    min-height: 58px !important;
    padding: 0.9rem 1.45rem !important;
    border: 1px solid #dfe4ea !important;
    border-radius: 12px !important;
    background: #f8fafc !important;
    box-shadow: 0 2px 8px rgba(15, 23, 42, 0.06) !important;
    transition: all 0.18s ease !important;
}

/* Chữ trong tab */
button[data-baseweb="tab"] p {
    font-size: 1.18rem !important;
    font-weight: 700 !important;
    line-height: 1.2 !important;
