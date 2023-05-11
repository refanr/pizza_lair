const searchBar = document.getElementById("search-bar");
const pizzaList = document.querySelector(".pizza");

searchBar.addEventListener("keyup", (event) => {
  const searchText = event.target.value.trim();

  if (searchText.length > 0) {
    fetch(`/pizza/search/${searchText}`)
      .then((response) => response.text())
      .then((html) => {
        pizzaList.innerHTML = html;
      });
  } else {
    fetch("/pizza/")
      .then((response) => response.text())
      .then((html) => {
        pizzaList.innerHTML = html;
      });
  }
});
