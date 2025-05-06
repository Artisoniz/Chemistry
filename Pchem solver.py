import streamlit as st


st.set_page_config(page_title= "P. Chem Solver", layout = "centered")

st.title(" Physical Chemistry Problem Solver ")
st.write(" Select a problem type and enter data ")

problem_type = st.selectbox(
    "Choose a problem type:",
    ["Gibbs Free Energy (^G)", "Ideal Gas Law (PV=nRT)", "Coming soon: Kinetics", "Coming soon: Quantum Mechanics"]
)

if problem_type == "Gibbs Free Energy (^G)":
    st.header(" ^G = ^H -T^S")

    delta_h = st.number_input(" ^H (Enthalpy change) in kJ/mol:", value = 0.0, format="%f")
    delta_s = st.number_input(" ^S (Entropy change) in kJ/mol * K:", value = 0.0, format="%f")
    temperature = st.number_input("Temperature in Kelvin (K):", value=298.15, format="%f")

    if st.button("Solve for ^G"):
        delta_g = delta_h - temperature * delta_s
        st.success(f"^G = {delta_g: .4f} kJ/mol")

        if delta_g < 0:
            st.markdown(" **Spontaneous rxn** (^G < 0")
        elif delta_g > 0:
            st.markdown(" **Non-spontanous rxn** (^G > 0)")
        else:
            st.markdown(" **Equilibrium rxn** (^G = 0)")

elif problem_type == "Ideal Gas Law (PV=nRT)":
    st.header("PV = nRT")

    pressure = st.number_input("Pressure (atm):", value = 1.0, format = "%f")
    volume = st.number_input("Volume (L):", value = 1.0, format = "%f" )
    moles = st.number_input("Moles of gas (n):", value = 1.0, format = "%f")
    r = .08206  #atm*L/mol*K

    if st.button("Calculate Temperature"):
        if moles !=0:
            temperature = (pressure * volume) / (moles * r)
            st.success(f"Temperature = {temperature: .2f} K")
        else:
            st.error("Number of moles cannot be zero.")
else:
    st.info("That module is coming soon. Stay tuned!")