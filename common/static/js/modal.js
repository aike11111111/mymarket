document.addEventListener('DOMContentLoaded', function() {
    const addButtons = document.querySelectorAll('.add-product');
    const modalTitle = document.querySelector('.modal-title');
    const modalBody = document.querySelector('.modal-body');
    const carritoProductos = document.getElementById('carrito-productos');
    const totalCarrito = document.getElementById('total-carrito'); 

    let carrito = JSON.parse(localStorage.getItem('carrito')) || [];

    const actualizarCarritoLocalStorage = () => {
        localStorage.setItem('carrito', JSON.stringify(carrito));
    };

    const calcularTotalCarrito = () => {
        let total = 0;
        carrito.forEach(producto => {
            total += producto.precio * producto.cantidad;
        });
        return total;
    };

    const cargarCarritoDesdeLocalStorage = () => {
        carritoProductos.innerHTML = '';
        carrito.forEach((producto, index) => {
            const listItem = document.createElement('li');
            listItem.classList.add('carrito-item');
            listItem.innerHTML = `  
                <img src="${producto.imagen}" alt="Producto">
                <div>
                    <button class="eliminar-producto" data-index="${index}">x</button>
                    <h6>${producto.nombre}</h6>
                    <p>Precio: $${producto.precio}</p>
                    <p>Cantidad: ${producto.cantidad}</p>
                </div>
            `;
            carritoProductos.appendChild(listItem);
        });

        totalCarrito.textContent = `Total: $${calcularTotalCarrito()}`;
    };

    cargarCarritoDesdeLocalStorage();

    carritoProductos.addEventListener('click', function(event) {
        if (event.target.classList.contains('eliminar-producto')) {
            const index = parseInt(event.target.getAttribute('data-index'));
            actualizarCarritoLocalStorage(); 

            cargarCarritoDesdeLocalStorage();
        }
    });

    addButtons.forEach(button => {
        button.addEventListener('click', function() {
            const productName = this.getAttribute('data-name');
            const productPrice = parseFloat(this.getAttribute('data-price'));
            const productImage = this.getAttribute('data-image');
            const productQuantity = parseInt(this.parentElement.querySelector('.producto-cantidad').value);

            let productoExistente = carrito.find(item => item.nombre === productName);

            if (productoExistente) {

                productoExistente.cantidad += productQuantity;
            } else {

                const producto = {
                    imagen: productImage,
                    nombre: productName,
                    precio: productPrice,
                    cantidad: productQuantity
                };

                carrito.push(producto);
            }

            actualizarCarritoLocalStorage();

            carritoProductos.innerHTML = '';

            cargarCarritoDesdeLocalStorage();
        });
    });
});
