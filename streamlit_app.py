import streamlit as st
import pyodbc

# SQL Server 数据库连接配置
def get_db_connection():
    conn_str = (
        "DRIVER={SQL Server};"
        "SERVER=1.tcp.nas.cpolar.cn:10264;"  # 替换为你的服务器名称
        "DATABASE=test;"  # 替换为你的数据库名称
        "UID=sa;"  # 替换为你的数据库用户名
        "PWD=suphie8639;"  # 替换为你的数据库密码
    )
    return pyodbc.connect(conn_str)

# 验证用户名和密码
def authenticate(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user is not None

# 主应用逻辑
def main():
    st.title("秀衫衫查看成本表登录界面")

    # 初始化 session_state
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    # 如果未登录，显示登录表单
    if not st.session_state.logged_in:
        username = st.text_input("用户名")
        password = st.text_input("密码", type="password")

        if st.button("登录"):
            if authenticate(username, password):
                st.session_state.logged_in = True
                st.session_state.username = username
                st.success("登录成功！")
            else:
                st.error("用户名或密码错误")

    # 如果已登录，显示数据界面
    if st.session_state.logged_in:
        st.title(f"欢迎, {st.session_state.username}!")
        st.write("这是数据界面。")

        if st.button("退出"):
            st.session_state.logged_in = False
            st.session_state.username = None
            st.rerun()  # 使用 st.rerun() 刷新页面

# 运行应用
if __name__ == "__main__":
    main()
