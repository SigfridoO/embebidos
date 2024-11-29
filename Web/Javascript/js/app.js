console.log("hola mundo");

const numero = 3;
console.log(numero)

const nombre = "Jesús";
console.log(nombre)

const altura = 1.70;
console.log(altura);

let resultado = 6;
console.log({resultado});

resultado = 8;
console.log({resultado});


const alumnos = ['Denisse', 'Bryant', 'Adair', 'Kevin', 'Jesús', 'Ignacio', 'Alejandra'];
console.log({...alumnos});
console.log(alumnos.sort());

for ( let entradas of alumnos.entries()){
    console.log(entradas);
}

for ( let keys of alumnos.keys()){
    console.log(keys);
}

for ( let valores of alumnos.values()){
    console.log(valores);
}

console.log(alumnos.length);

let elemento = alumnos.pop();
console.log(elemento);
console.log(alumnos);

alumnos.push("Victor");
console.log(alumnos);

console.log(alumnos.at(2));
// Objetos de Javascript
const aaron  = {
    nombre: "Aaron",
    apellido: "Barragan",
    edad: "21",
    estatura: 1.80,

    asistira : function () {
        return "Si";
    }
    
};

console.log(aaron);
console.log(aaron.edad);
console.log(aaron.asistira);

// Funciones
function calcularCostoProyecto( materiales, manoDeObra) {
    return   materiales + manoDeObra;
}

const calcularCosto2 = (materiales, manoDeObra) =>{
    return   materiales + manoDeObra;
}

let costo = calcularCostoProyecto(100, 300);

costo = calcularCostoProyecto(100, 300);
console.log("calcularCostoProyecto: ", costo);

console.error("calcularCosto2:", calcularCosto2(100, 300));

const saludar  = nombre => {
    return `Hola mi nombre es ${nombre}`;
}

console.log(saludar("Arturo"));

alumnos.forEach( alumno => {
    console.log(saludar(alumno));})