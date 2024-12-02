const SALA_CHAT = 'python';
const SERVIDOR_CHAT = window.location.host; // Función para obtener la dirección del servidor
const PROTOCOLO_WS = window.location.protocol === 'https:' ? 'wss://' : 'ws://';
const chatSocket = new WebSocket(PROTOCOLO_WS + SERVIDOR_CHAT + '/ws/chat/' + SALA_CHAT + '/');

const campoNombre = document.querySelector('#nombre');
const mensajes = document.querySelector('#mensajes');
const campoTexto = document.querySelector('#texto');
const botonEnviar = document.querySelector('#enviar');

function anyadirNuevoMensajeAlHTML(nombre, texto, propio = false) {
    const miContenedor = document.createElement('div');
    miContenedor.classList.add('card', 'mb-3', propio ? 'bg-primary' : 'bg-secondary', 'text-white');

    const miNombre = document.createElement('div');
    miNombre.classList.add('card-header', 'font-weight-bold');
    miNombre.textContent = nombre;
    miContenedor.appendChild(miNombre);
    
    const miTexto = document.createElement('div');
    miTexto.classList.add('card-body');
    const miTextoParrafo = document.createElement('p');
    miTextoParrafo.classList.add('card-text');
    miTextoParrafo.textContent = texto;
    miTexto.appendChild(miTextoParrafo);
    miContenedor.appendChild(miTexto);
    
    mensajes.appendChild(miContenedor);
    mensajes.scrollTop = mensajes.scrollHeight;
}

function enviarNuevoMensaje() {
    // Envia al WebSocket un nuevo mensaje
    if (campoTexto.value.trim() !== '') {
        chatSocket.send(JSON.stringify({
            name: campoNombre.value,
            text: campoTexto.value
        }));
        // Limpiamos el campo donde hemos escrito
        campoTexto.value = '';
        // Le volvemos a dar el foco para escribir otro mensaje
        campoTexto.focus();
    }
}

// Conectado
chatSocket.addEventListener('open', () => {
    console.log('Conectado');
});
// Desconectado
chatSocket.addEventListener('close', () => {
    console.log('Desconectado');
});

// Recibir mensaje
chatSocket.addEventListener('message', (event) => {
    console.log('Recibido nuevo mensaje');
    const miNuevaData = JSON.parse(event.data);
    anyadirNuevoMensajeAlHTML(miNuevaData.name, miNuevaData.text, miNuevaData.name === campoNombre.value);
});

// Enviar mensaje cuando se pulsa en el botón Enviar
botonEnviar.addEventListener('click', enviarNuevoMensaje);

// Enviar mensaje cuando se pulsa en el teclado Enter
campoTexto.addEventListener('keyup', (e) => e.keyCode === 13 ? enviarNuevoMensaje() : false);
