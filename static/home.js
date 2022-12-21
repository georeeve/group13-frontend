[...document.getElementsByClassName("add-item")].forEach((form) => {
  form.addEventListener("submit", (e) => addToBasket(form, e));
});

updateBasketPill();

async function addToBasket(form, e) {
  e.preventDefault();
  const formData = new FormData(form);

  const itemId = form.id.split("item-")[1];
  const quantity = formData.get("quantity");
  await fetch("/add", {
    method: "POST",
    body: JSON.stringify({ itemId, quantity }),
    headers: { "Content-Type": "application/json" },
  });
  updateBasketPill();
}

function getCookie(name) {
  function escape(s) {
    return s.replace(/([.*+?\^$(){}|\[\]\/\\])/g, "\\$1");
  }
  const match = document.cookie.match(
    RegExp("(?:^|;\\s*)" + escape(name) + "=([^;]*)")
  );
  return match ? match[1] : null;
}

function updateBasketPill() {
  const cookie = getCookie("basket");
  if (cookie == null) {
    return;
  }

  const basket = JSON.parse(atob(cookie));

  if (Object.keys(basket).length === 0) {
    return;
  }

  const currentItems = Object.values(basket).reduce(
    (prev, curr) => prev + curr
  );

  const basketPill = document.getElementById("basket-quantity");

  if (basketPill.textContent === "0") {
    basketPill.classList.add("d-none");
  } else {
    basketPill.classList.remove("d-none");
    basketPill.textContent = currentItems;
  }
}
