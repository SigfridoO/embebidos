const alumnos = ['Javier', 'Angel', 'Chucho', 'Koko', 'yisus', 'Nacho', 'Alexis', 'Mauren'];

// console.table(alumnos);

// console.warn('For tradicional');
// for (let i = 0; i < alumnos.length; i++) {
//     console.log(alumnos[i]);
// }

// console.warn('For in');
// for (let i in alumnos) {
//     console.log(alumnos[i]);
// }

// console.warn('For each');
// for (let alumno in alumnos) {
//     console.log(alumno);
// }


const contenedorNombres = document.getElementById("contenedor-nombres");
// console.log(contenedorNombres);

function mostrarNombres() {
    let html = '';
    setTimeout(() => {
        console.log("Dentro de la función mostrar nombres");
        alumnos.forEach(alumno => {
            html += `<li>${alumno}</li>`;
        })
        contenedorNombres.innerHTML = html;
    }
    , 3000);
}

mostrarNombres();