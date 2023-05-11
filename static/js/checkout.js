function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

document.querySelectorAll('.add-pizza').forEach(function(button) {
    button.addEventListener('click', function() {
        let pizzaId = this.getAttribute('data-pizza-id');
        let pizzaPrice = parseFloat(this.getAttribute('data-pizza-price'));

        // Make a request to your Django view
        fetch(`/checkout/add_pizza/${pizzaId}/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken') // Include CSRF token if needed
            }
        }).then(response => {
            if (response.ok) {
                let quantityElement = document.querySelector('.quantity[data-pizza-id="' + pizzaId + '"]');
                let quantity = parseInt(quantityElement.textContent.split('x ')[1]);
                quantityElement.textContent = 'Quantity: x ' + (quantity + 1);
                let totalPriceElement = document.getElementById('total-price');
                let totalPrice = parseFloat(totalPriceElement.textContent);
                totalPriceElement.textContent = (totalPrice + pizzaPrice).toFixed(2);
           } else {
                // Handle error
            }
        });
    });
});

document.querySelectorAll('.remove-pizza').forEach(function(button) {
    button.addEventListener('click', function() {
        let pizzaId = this.getAttribute('data-pizza-id');
        let pizzaPrice = parseFloat(this.getAttribute('data-pizza-price'));

        // Make a request to your Django view
        fetch(`/checkout/remove_pizza/${pizzaId}/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken') // Include CSRF token if needed
            }
        }).then(response => {
            if (response.ok) {
                let quantityElement = document.querySelector('.quantity[data-pizza-id="' + pizzaId + '"]');
                let quantity = parseInt(quantityElement.textContent.split('x ')[1]);
                if (quantity > 0) {
                    quantityElement.textContent = 'Quantity: x ' + (quantity - 1);
                }
                let totalPriceElement = document.getElementById('total-price');
                let totalPrice = parseFloat(totalPriceElement.textContent);
                if (totalPrice >= pizzaPrice) {
                    totalPriceElement.textContent = (totalPrice - pizzaPrice).toFixed(2);
                }
            } else {
                // Handle error
            }
        });
    });
});
