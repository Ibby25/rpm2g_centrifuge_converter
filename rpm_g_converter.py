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
st.title("Centrifuge RPM ↔ G-Force Converter")

# Mode selection
mode = st.radio("Select conversion mode:", ["RPM → G-Force", "G-Force → RPM"])

# Radius input units
unit = st.radio("Radius units:", ["meters (m)", "centimeters (cm)"])

# RPM → G mode
if mode == "RPM → G-Force":
    rpm = st.number_input("Enter RPM", min_value=0.0, step=10.0)
    radius = st.number_input(f"Enter radius ({unit.split()[0]})", min_value=0.0, step=0.01)

    # Convert radius to meters if cm
    radius_m = radius / 100 if "cm" in unit else radius

    st.markdown(r"**Formula:** $RCF = \frac{(2 \pi \cdot RPM / 60)^2 \cdot r}{9.81}$")

    if rpm > 0 and radius_m > 0:
        gs = rpm_to_g(rpm, radius_m)
        st.write(f"At **{rpm:,.2f} RPM** and radius **{radius:.2f} {unit.split()[0]}**:")
        st.success(f"Centrifugal force ≈ **{gs:,.2f} × g**")

# G → RPM mode
elif mode == "G-Force → RPM":
    gs = st.number_input("Enter g-force (× g)", min_value=0.0, step=10.0)
    radius = st.number_input(f"Enter radius ({unit.split()[0]})", min_value=0.0, step=0.01)

    # Convert radius to meters if cm
    radius_m = radius / 100 if "cm" in unit else radius

    st.markdown(r"**Formula:** $RPM = \frac{\sqrt{g_{force} \cdot 9.81 / r} \cdot 60}{2\pi}$")

    if gs > 0 and radius_m > 0:
        rpm = g_to_rpm(gs, radius_m)
        st.write(f"For **{gs:,.2f} × g** at radius **{radius:.2f} {unit.split()[0]}**:")
        st.success(f"Required speed ≈ **{rpm:,.2f} RPM**")

