

class Sensor {
    constructor(nombre, valor) {
        this.nombre = nombre;
        this.valor = valor;
        console.log("Se ha creado el sensor");
    }

    registrarValor(numero) {
        if (numero <= 30) {
            console.log("Es nivel es bajo");
        } else if (numero > 120){ 
               console.log("El nivel es muy alto");
        }
    }
    static mosTrarInicio () {
        console.log("Inicializando el sensor");
    }

}

//const sensorTemperatura = new Sensor("Sensor de temperatura", 0);
// sensorTemperatura.registrarValor(24);

Sensor.mosTrarInicio();

// console.log(sensorTemperatura);


// /Herencia

class SensorConActuador extends Sensor{
    constructor(nombre, valor, actuador) {
        super(nombre, valor);
        this.actuador = actuador;
        console.log("Se ha creado el sensor con actuador");
    }

}

sensorConActuador = new SensorConActuador("sensor de flujo", 0, "vá                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    GUIASdesmos
