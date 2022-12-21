const params = new Proxy(new URLSearchParams(window.location.search), {
  get: (searchParams, prop) => searchParams.get(prop),
});

const paginationPrev = document.getElementById("pagination-prev");
const paginationNext = document.getElementById("pagination-next");
const paginationPages = [...document.getElementsByClassName("page-num")];

if (Number(params.start) < 24) {
  paginationPrev.classList.add("disabled");
} else {
  paginationPrev.classList.remove("disabled");
}

if (Number(params.start) >= Number(params.length) - 24) {
  paginationNext.classList.add("disabled");
} else {
  paginationNext.classList.remove("disabled");
}

const desktopMediaQuery = window.matchMedia("(min-width: 520px)");
function handleDesktopSize(e) {
  if (e.matches) {
    paginationPages.forEach((element) => {
      if (Number(element.id) === Number(params.start) / 24) {
        element.classList.add("active");
      }
    });
  }
}
desktopMediaQuery.addEventListener("change", handleDesktopSize);
handleDesktopSize(desktopMediaQuery);

const mobileMediaQuery = window.matchMedia("(max-width: 519px)");
function handleSmallerSize(e) {
  if (e.matches) {
    paginationPages.forEach((element) => {
      element.classList.remove("active");
    });
  }
}

mobileMediaQuery.addEventListener("change", handleSmallerSize);
handleSmallerSize(mobileMediaQuery);

// function showModal() {
const logOutModal = new bootstrap.Modal(
  document.getElementById("log-out-modal")
);

function showModal(isLoggedOut) {
  if (isLoggedOut) logOutModal.show();
}
