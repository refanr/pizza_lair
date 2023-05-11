  const searchInput = document.getElementById('searchInput');
  const cards = document.getElementsByClassName('card');

  searchInput.addEventListener('keyup', () => {
    const searchTerm = searchInput.value.toLowerCase();
    for (const card of cards) {
      const pizzaName = card.querySelector('.card-body a').textContent.toLowerCase();
      if (pizzaName.includes(searchTerm)) {
        card.style.display = '';
      } else {
        card.style.display = 'none';
      }
    }
  });
