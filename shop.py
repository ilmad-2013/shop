import streamlit as st

st.set_page_config(
    page_title="Smart Shopping Assistant",
    page_icon="🛒"
)

st.title("🛒 Smart Shopping Assistant")
st.write("Plan your shopping without going over budget.")

# Product database
products = {
    "Notebook": 1500,
    "Pen Pack": 1000,
    "Water Bottle": 3500,
    "School Bag": 12000,
    "Calculator": 6500,
    "Headphones": 8500,
    "Lunch Box": 4000,
    "Desk Lamp": 7000
}

# Store cart
if "cart" not in st.session_state:
    st.session_state.cart = {}

# Budget
st.subheader("💰 Set Your Budget")

budget = st.number_input(
    "How much do you want to spend?",
    min_value=0.0,
    value=20000.0,
    step=1000.0
)

st.divider()

# Product selection
st.subheader("🛍️ Choose a Product")

product = st.selectbox(
    "Product:",
    list(products.keys())
)

st.write(
    f"Price: ₦{products[product]:,.0f}"
)

quantity = st.number_input(
    "Quantity:",
    min_value=1,
    max_value=20,
    value=1
)

if st.button("Add to Cart"):

    if product in st.session_state.cart:

        st.session_state.cart[product] += quantity

    else:

        st.session_state.cart[product] = quantity

    st.success(
        f"{quantity} × {product} added to your cart!"
    )

st.divider()

# Shopping cart
st.subheader("🛒 Your Cart")

if len(st.session_state.cart) == 0:

    st.info("Your cart is empty.")

else:

    total = 0

    for item, quantity in st.session_state.cart.items():

        price = products[item]

        item_total = price * quantity

        total += item_total

        st.write(
            f"**{item}** — "
            f"{quantity} × ₦{price:,.0f} "
            f"= ₦{item_total:,.0f}"
        )

    st.divider()

    st.metric(
        "Shopping Total",
        f"₦{total:,.0f}"
    )

    # Compare with budget
    if total > budget:

        difference = total - budget

        st.error(
            f"You are ₦{difference:,.0f} over budget!"
        )

    elif total == budget:

        st.success(
            "Perfect! You are exactly on budget."
        )

    else:

        remaining = budget - total

        st.success(
            f"You have ₦{remaining:,.0f} left."
        )

    # Percentage of budget
    if budget > 0:

        percentage = total / budget

        st.write("Budget used:")

        st.progress(
            min(percentage, 1.0)
        )

        st.write(
            f"{percentage * 100:.1f}% of your budget"
        )

    if st.button("Clear Cart"):

        st.session_state.cart = {}

        st.rerun()