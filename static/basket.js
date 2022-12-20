[...document.getElementsByClassName("add-item")].forEach(form => {
    form.addEventListener("submit", (e) => addToBasket(form, e));
});

function addToBasket(form, e) {
    e.preventDefault();
    const basket = JSON.parse(localStorage.getItem("basket")) ?? { };
    const formData = new FormData(form);

    const itemId = form.id.split("item-")[1];
    const currentQuantity = parseInt(basket[itemId]) || 0;
    const toAddQuantity = parseInt(formData.get("quantity"));
    basket[itemId] = currentQuantity + toAddQuantity;
    localStorage.setItem("basket", JSON.stringify(basket));
}
