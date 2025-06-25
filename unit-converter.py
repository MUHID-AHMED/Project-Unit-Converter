import streamlit as st

# Set page title
st.set_page_config(page_title="Unit Converter", layout="centered")

# Title of the application
st.title("🔢 Unit Converter")

# Conversion type dropdown
conversion_type = st.selectbox("Choose a conversion type", ["Length", "Weight", "Temperature"])

# Input for value
value = st.number_input("Enter the value to convert", min_value=0.0, format="%.2f")

# Dropdowns for 'From' and 'To' units (default: meters to centimeters)
if conversion_type == "Length":
    units = ["Meter", "Centimeter", "Kilometer", "Inch", "Foot"]
elif conversion_type == "Weight":
    units = ["Kilogram", "Gram", "Pound", "Ounce"]
elif conversion_type == "Temperature":
    units = ["Celsius", "Fahrenheit", "Kelvin"]

from_unit = st.selectbox("From", units)
to_unit = st.selectbox("To", units)

# Conversion functions
def convert_units(value, from_unit, to_unit, conversion_type):
    if conversion_type == "Length":
        conversion_factors = {
            "Meter": 1, "Centimeter": 100, "Kilometer": 0.001,
            "Inch": 39.3701, "Foot": 3.28084
        }
    
    elif conversion_type == "Weight":
        conversion_factors = {
            "Kilogram": 1, "Gram": 1000, "Pound": 2.20462, "Ounce": 35.274
        }

    elif conversion_type == "Temperature":
        if from_unit == to_unit:
            return value
        if from_unit == "Celsius":
            return value * 9/5 + 32 if to_unit == "Fahrenheit" else value + 273.15
        if from_unit == "Fahrenheit":
            return (value - 32) * 5/9 if to_unit == "Celsius" else ((value - 32) * 5/9) + 273.15
        if from_unit == "Kelvin":
            return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32
    
    # Convert value
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

# ✅ Single "Convert" button
if st.button("Convert"):
    try:
        result = convert_units(value, from_unit, to_unit, conversion_type)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
    except Exception as e:
        st.error(f"Error: {e}")
