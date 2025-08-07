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

# Streamlit UI
st.title("RPM ↔ G-Force Centrifuge Converter")

st.markdown("### Step 1: Convert RPM to G-Force")
rpm1 = st.number_input("Enter the RPM of the first machine", min_value=0.0, step=10.0)
radius1 = st.number_input("Enter the radius of the first machine's disk (m)", min_value=0.0, step=0.01)

if rpm1 > 0 and radius1 > 0:
    gs = rpm_to_g(rpm1, radius1)
    st.success(f"That corresponds to approximately **{gs:.2f} g** of centrifugal acceleration.")

    st.markdown("### Step 2: Convert G-Force to RPM for Second Machine")
    radius2 = st.number_input("Enter the radius of the second machine's disk (m)", min_value=0.0, step=0.01)
    
    if radius2 > 0:
        rpm2 = g_to_rpm(gs, radius2)
        st.success(f"To achieve the same g-force on the second machine, set it to approximately **{rpm2:.2f} RPM**.")
