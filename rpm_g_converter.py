import streamlit as st
import math

# Conversion functions
def rpm_to_g(rpm, radius_m):
    ang_v_omega = 2 * math.pi * rpm / 60
    accel = ang_v_omega ** 2 * radius_m
    return accel / 9.81

def g_to_rpm(gs, radius_m):
    accel = gs * 9.81
    ang_v_omega = math.sqrt(accel / radius_m)
    return ang_v_omega * 60 / (2 * math.pi)

# App title
st.title("⚙️ Centrifuge RPM ↔ G-Force Converter")

# Mode selection
mode = st.radio("Select conversion mode:", ["RPM → G-Force", "G-Force → RPM"])
unit = st.radio("Radius units:", ["meters (m)", "centimeters (cm)"])

# Conversion: RPM → G
if mode == "RPM → G-Force":
    rpm1 = st.number_input("Enter RPM of centrifuge 1", min_value=0.0, step=10.0)
    radius1 = st.number_input(f"Enter radius of centrifuge 1 ({unit.split()[0]})", min_value=0.0, step=0.01)
    radius1_m = radius1 / 100 if "cm" in unit else radius1

    st.markdown(r"**Formula:** $RCF = \frac{(2 \pi \cdot RPM / 60)^2 \cdot r}{9.81}$")

    if rpm1 > 0 and radius1_m > 0:
        gs = rpm_to_g(rpm1, radius1_m)
        st.success(f"Centrifuge 1: {rpm1:,.2f} RPM → **{gs:,.2f} × g**")

        st.subheader("Match this g-force on another centrifuge")
        radius2 = st.number_input(f"Enter radius of centrifuge 2 ({unit.split()[0]})", min_value=0.0, step=0.01)
        radius2_m = radius2 / 100 if "cm" in unit else radius2

        if radius2_m > 0:
            rpm2 = g_to_rpm(gs, radius2_m)
            st.info(f"Centrifuge 2 needs ≈ **{rpm2:,.2f} RPM** to match {gs:,.2f} × g")

# Conversion: G → RPM
elif mode == "G-Force → RPM":
    gs = st.number_input("Enter g-force (× g)", min_value=0.0, step=10.0)
    radius1 = st.number_input(f"Enter radius of centrifuge 1 ({unit.split()[0]})", min_value=0.0, step=0.01)
    radius1_m = radius1 / 100 if "cm" in unit else radius1

    st.markdown(r"**Formula:** $RPM = \frac{\sqrt{g_{force} \cdot 9.81 / r} \cdot 60}{2\pi}$")

    if gs > 0 and radius1_m > 0:
        rpm1 = g_to_rpm(gs, radius1_m)
        st.success(f"Centrifuge 1: **{gs:,.2f} × g** → {rpm1:,.2f} RPM")

        st.subheader("Match this g-force on another centrifuge")
        radius2 = st.number_input(f"Enter radius of centrifuge 2 ({unit.split()[0]})", min_value=0.0, step=0.01)
        radius2_m = radius2 / 100 if "cm" in unit else radius2

        if radius2_m > 0:
            rpm2 = g_to_rpm(gs, radius2_m)
            st.info(f"Centrifuge 2 needs ≈ **{rpm2:,.2f} RPM** to match {gs:,.2f} × g")
