import streamlit as st

def length_convert(value, from_unit, to_unit):
    conversions = {
        "Meters": 1,
        "Kilometers": 0.001,
        "Centimeters": 100,
        "Millimeters": 1000,
        "Feet": 3.28,
        "Inches": 39.37
    }
    return value*(conversions[to_unit]/conversions[from_unit])
def weight_convert(value, from_unit, to_unit):
    conversions = {
        "Grams": 1,
        "Kilograms": 0.001,
        "Pounds": 0.002,
    }
    return value * (conversions[to_unit] / conversions[from_unit])
def time_convert(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    elif from_unit == "Hours" and to_unit == "Seconds":
      return value*3600
    elif from_unit == "Hours" and to_unit == "Minutes" or from_unit == "Minutes" and to_unit == "Seconds":
      return value*60
    elif from_unit == "Hours" and to_unit == "Days":
      return value/24
    elif from_unit == "Minutes" and to_unit == "Hours" or from_unit == "Seconds" and to_unit == "Minutes":
      return value/60
    elif from_unit == "Minutes" and to_unit == "Days":
      return value/1440
    elif from_unit == "Seconds" and to_unit == "Hours":
      return value/3600
    elif from_unit == "Seconds" and to_unit == "Days":
      return value/86400
def temp_convert(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    if from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    if from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    if from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    return value

st.title("Unit Converter")
st.write("Convert values across different units effortlessly!")

category = st.sidebar.selectbox("## Select Category", ["Length", "Weight", "Temperature","Time"])
st.sidebar.markdown("## Created by Khawaja Abdul Moiz")
st.sidebar.write("Catch me on 👇")
st.sidebar.markdown("### [👉 **LinkedIn**](https://www.linkedin.com/in/khawaja-abdul-moiz)", unsafe_allow_html=True)
st.sidebar.markdown("### [💻 **GitHub**](https://github.com/KhawajaAbdulMoiz)", unsafe_allow_html=True)
st.sidebar.markdown("### [🌐 **My Portfolio**](https://khawajaabdulmoiz.vercel.app/)", unsafe_allow_html=True)

if category == "Length":
    from_unit = st.selectbox("## From", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Feet", "Inches"])
    to_unit = st.selectbox("## To", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Feet", "Inches"])
    value = st.number_input("## Enter Value", min_value=0.0, format="%.1f")
    if st.button("Convert"):
        st.success(f"Converted Value : {length_convert(value, from_unit, to_unit) :.1f} {to_unit}")

elif category == "Weight":
    from_unit = st.selectbox("From", ["Grams", "Kilograms", "Pounds", "Ounces"])
    to_unit = st.selectbox("To", ["Grams", "Kilograms", "Pounds", "Ounces"])
    value = st.number_input("Enter Value", min_value=0.0, format="%.1f")
    if st.button("Convert"):
        st.success(f"Converted Value : {weight_convert(value, from_unit, to_unit) :.1f} {to_unit}")

elif category == "Temperature":
    from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])
    value = st.number_input("Enter Value", format="%.2f")
    if st.button("Convert"):
        st.success(f"Converted Value : {temp_convert(value, from_unit, to_unit) :.1f} {to_unit}")
elif category == "Time":
   from_unit = st.selectbox("From", ["Hours", "Minutes", "Days"])
   to_unit = st.selectbox("To", ["Minutes", "Hours", "Days"])
   value = st.number_input("Enter Value", format="%.2f")
   if st.button("Convert"):
      st.success(f"Converted Value : {time_convert(value,from_unit,to_unit) :.1f} {to_unit}")
