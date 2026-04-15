// Esperamos a que la página cargue completamente antes de ejecutar JS
document.addEventListener('DOMContentLoaded', function() {
    // ==========================================
    // 1. VALIDACIONES: REGISTRO DE USUARIO (Feedback Inline)
    // ==========================================
    const formRegistro = document.getElementById('formularioRegistro');
    
    if (formRegistro) {
        formRegistro.addEventListener('submit', function(evento) {
            evento.preventDefault(); // Detenemos el envío

            // Capturamos los inputs completos (no solo su valor) para poder pintarlos
            const inputNombre = document.getElementById('nombre');
            const inputUsuario = document.getElementById('usuario');
            const inputCorreo = document.getElementById('correo');
            const inputDireccion = document.getElementById('direccion');
            const inputClave = document.getElementById('clave');
            const inputRepetirClave = document.getElementById('repetirClave');
            const inputFecha = document.getElementById('fechaNac');
            const mensajeExito = document.getElementById('mensajeExitoGlobal');

            let formularioValido = true; // Asumimos que todo está bien hasta demostrar lo contrario

            // Escondemos el mensaje de éxito por si estaba visible
            mensajeExito.classList.add('d-none');

            // --- Validación Nombre ---
            if (inputNombre.value.trim() === '') {
                marcarInvalido(inputNombre);
                formularioValido = false;
            } else {
                marcarValido(inputNombre);
            }

            // --- Validación Usuario (Mínimo 4) ---
            if (inputUsuario.value.trim().length < 4) {
                marcarInvalido(inputUsuario);
                formularioValido = false;
            } else {
                marcarValido(inputUsuario);
            }

            // --- Validación Correo ---
            const regexCorreo = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!regexCorreo.test(inputCorreo.value.trim())) {
                marcarInvalido(inputCorreo);
                formularioValido = false;
            } else {
                marcarValido(inputCorreo);
            }

            // --- Validación Dirección ---
            if (inputDireccion.value.trim() === '') {
                marcarInvalido(inputDireccion);
                formularioValido = false;
            } else {
                marcarValido(inputDireccion);
            }

            // --- Validación Contraseña (6 a 18 chars, mayúscula, número, especial) ---
            const regexClave = /^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+{}\[\]:;<>,.?~\\-]).{6,18}$/;
            if (!regexClave.test(inputClave.value)) {
                marcarInvalido(inputClave);
                formularioValido = false;
            } else {
                marcarValido(inputClave);
            }

            // --- Validación Repetir Contraseña ---
            if (inputRepetirClave.value === '' || inputRepetirClave.value !== inputClave.value) {
                marcarInvalido(inputRepetirClave);
                formularioValido = false;
            } else {
                marcarValido(inputRepetirClave);
            }

            // --- Validación Edad (Mínimo 13 años) ---
            if (inputFecha.value === '') {
                marcarInvalido(inputFecha);
                formularioValido = false;
            } else {
                const fechaNacimiento = new Date(inputFecha.value);
                const hoy = new Date();
                let edad = hoy.getFullYear() - fechaNacimiento.getFullYear();
                const diferenciaMeses = hoy.getMonth() - fechaNacimiento.getMonth();
                if (diferenciaMeses < 0 || (diferenciaMeses === 0 && hoy.getDate() < fechaNacimiento.getDate())) {
                    edad--;
                }

                if (edad < 13) {
                    marcarInvalido(inputFecha);
                    formularioValido = false;
                } else {
                    marcarValido(inputFecha);
                }
            }

            // Si TODO está correcto (formularioValido sigue siendo true)
            if (formularioValido) {
                mensajeExito.classList.remove('d-none');
            }
        });
    }

    // =======================
    // 2. VALIDACIONES: LOGIN 
    // =======================
    const formLogin = document.getElementById('formularioLogin');
    if (formLogin) {
        formLogin.addEventListener('submit', function(e) {
            e.preventDefault();
            const inputUsuario = document.getElementById('loginUsuario');
            const inputClave = document.getElementById('loginClave');
            const cajaError = document.getElementById('mensajeErrorLogin');
            
            let formularioValido = true;
            cajaError.classList.add('d-none');

            // Validar Usuario
            if (inputUsuario.value.trim() === '') {
                marcarInvalido(inputUsuario);
                formularioValido = false;
            } else {
                marcarValido(inputUsuario);
            }

            // Validar Clave
            if (inputClave.value === '') {
                marcarInvalido(inputClave);
                formularioValido = false;
            } else {
                marcarValido(inputClave);
            }

            if (formularioValido) {
                cajaError.className = 'alert alert-success mt-3';
                cajaError.innerHTML = '¡Sesión iniciada correctamente!';
                cajaError.classList.remove('d-none');
            }
        });
    }

    // ==========================================
    // 3. VALIDACIONES: RECUPERAR CLAVE
    // ==========================================
    const formRecuperar = document.getElementById('formularioRecuperar');
    if (formRecuperar) {
        formRecuperar.addEventListener('submit', function(e) {
            e.preventDefault();
            const cajaError = document.getElementById('mensajeRecuperar');
            const correo = document.getElementById('recuperarCorreo').value.trim();

            if (!correo) {
                mostrarError(cajaError, 'Por favor, ingresa tu correo electrónico.');
                return;
            }

            cajaError.className = 'alert alert-success mt-3';
            cajaError.innerHTML = 'Te hemos enviado un enlace de recuperación. Revisa tu bandeja de entrada.';
            cajaError.classList.remove('d-none');
        });
    }

    // ============================
    // 4. VALIDACIONES: MANTENEDOR 
    // ============================
    const formMantenedor = document.getElementById('formularioMantenedor');
    if (formMantenedor) {
        formMantenedor.addEventListener('submit', function(e) {
            e.preventDefault();
            const inputNombre = document.getElementById('prodNombre');
            const inputCategoria = document.getElementById('prodCategoria');
            const inputPrecio = document.getElementById('prodPrecio');
            const inputStock = document.getElementById('prodStock');
            const cajaError = document.getElementById('mensajeErrorProducto');

            let formularioValido = true;
            cajaError.classList.add('d-none');

            // Validar Nombre
            if (inputNombre.value.trim() === '') {
                marcarInvalido(inputNombre);
                formularioValido = false;
            } else {
                marcarValido(inputNombre);
            }

            // Validar Categoría
            if (inputCategoria.value === '') {
                marcarInvalido(inputCategoria);
                formularioValido = false;
            } else {
                marcarValido(inputCategoria);
            }

            // Validar Precio
            if (inputPrecio.value === '' || inputPrecio.value <= 0) {
                marcarInvalido(inputPrecio);
                formularioValido = false;
            } else {
                marcarValido(inputPrecio);
            }

            // Validar Stock
            if (inputStock.value === '' || inputStock.value < 0) {
                marcarInvalido(inputStock);
                formularioValido = false;
            } else {
                marcarValido(inputStock);
            }

            if (formularioValido) {
                cajaError.className = 'alert alert-success mt-3 py-2';
                cajaError.innerHTML = '¡Producto agregado al inventario con éxito!';
                cajaError.classList.remove('d-none');
                formMantenedor.reset(); // Limpia el formulario tras guardar
                
                // Quitamos las clases verdes para que vuelva a su estado original
                inputNombre.classList.remove('is-valid');
                inputCategoria.classList.remove('is-valid');
                inputPrecio.classList.remove('is-valid');
                inputStock.classList.remove('is-valid');
            }
        });
    }

    // ==========================================
    // 5. SIMULACIÓN DE PAGO: CARRITO
    // ==========================================
    const btnPago = document.getElementById('btnSimularPago');
    if (btnPago) {
        btnPago.addEventListener('click', function() {
            const mensajePago = document.getElementById('mensajePago');
            mensajePago.classList.remove('d-none');
            btnPago.disabled = true; // Deshabilita el botón para no pagar dos veces
            btnPago.innerHTML = 'Procesando...';
            
            // Simulamos que carga por 1.5 segundos
            setTimeout(() => {
                btnPago.innerHTML = 'Pago Realizado';
                btnPago.classList.replace('btn-danger', 'btn-success');
            }, 1500);
        });
    }

    // --- FUNCIÓN AUXILIAR ---
    function mostrarError(elemento, mensaje) {
        elemento.className = 'alert alert-danger mt-3 py-2';
        elemento.innerHTML = mensaje;
        elemento.classList.remove('d-none');
    }

    // ================================
    // HERRAMIENTAS PARA PINTAR BORDES 
    // ================================
    function marcarInvalido(input) {
        input.classList.remove('is-valid');
        input.classList.add('is-invalid'); // Pone el borde rojo y muestra el texto
    }

    function marcarValido(input) {
        input.classList.remove('is-invalid');
        input.classList.add('is-valid'); // Pone el borde verde con el check
    }

});