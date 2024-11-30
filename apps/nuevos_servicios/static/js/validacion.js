$.validator.addMethod("validarut", function(value, element) {
    value = $.trim(value); 
    if (!/^[0-9]+[-|‐]{1}[0-9kK]{1}$/.test(value)) return false; 
    var tmp = value.split('-');
    var digv = tmp[1]; 
    var rut = tmp[0];
    if (digv == 'K') digv = 'k'; 
    var M = 0, S = 1;
    for (; rut; rut = Math.floor(rut / 10))
        S = (S + rut % 10 * (9 - M++ % 6)) % 11;
    return S ? S - 1 == digv : 'k' == digv;
}, "Por favor, ingrese un rut válido");

$.validator.addMethod("onlyletters", function(value, element) {
    return this.optional(element) || /^[a-zA-Z\sáéíóúÁÉÍÓÚñÑ]+$/.test(value);
}, "Este campo solo puede contener letras");

$.validator.addMethod("onlynumbers", function(value, element) {
    return this.optional(element) || /^\d+$/.test(value);
}, "Por favor, ingresa solo números en este campo");

$("#formulario").validate({
    rules:{
        nombre: {
            required: true,
            minlength: 3,
            maxlength: 20,
            onlyletters: true
        },
        apaterno: {
            required: true,
            minlength: 3,
            maxlength: 20,
            onlyletters: true
        },
        amaterno: {
            required: true,
            minlength: 3,
            maxlength: 20,
            onlyletters: true
        },
        rut: {
            required: true,
            minlength: 9,
            maxlength: 10,
            validarut: true
        },
        telefono: {
            required: true,
            minlength: 9,
            maxlength: 12,
            onlynumbers: true
        },
        direccion: {
            required: true,
            minlength: 10,
        },
        comuna: {
            required: true
        },
        mensaje: {
            required: true,
            minlength: 10,
            maxlength: 120,
        }
    },
    messages: {
        nombre: {
            required: "Por favor, ingrese su nombre",
            minlength:"El nombre debe tener minimo 3 caracteres",
            maxlength: "El nombre debe tener maximo 20 caracteres"
        },
        apaterno: {
            required: "Por favor, ingrese su apellido paterno",
            minlength: "El apellido paterno debe tener minimo 3 caracteres",
            maxlength: "El apellido paterno debe tener maximo 20 caracteres"
        },
        amaterno: {
            required: "Por favor, ingrese su apellido materno",
            minlength: "El apellido materno debe tener minimo 3 caracteres",
            maxlength: "El apellido materno debe tener maximo 20 caracteres"
        },
        rut: {
            required: "Por favor, ingresa su rut",
            minlength: "El rut debe tener minimo 9 caracteres",
            maxlength: "El rut debe tener maximo 10 caracteres"

        },
        telefono: {
            required: "Por favor, ingrese su telefono",
            minlength: "El celular debe tener minimo 9 caracteres",
            maxlength: "El celular debe tener maximo 12 caracteres"
        },
        direccion: {
            required: "Por favor, ingrese su dirección",
            minlength: "La dirección debe tener mínimo 10 caracteres"
        },
        comuna: {
            required: "Por favor, ingrese su comuna"
        },
        mensaje: {
            required: "Por favor, ingrese su mensaje",
            minlength: "El mensaje debe tener mínimo 10 caracteres",
            maxlength: "El mensaje debe tener maximo 120 caracteres"
        },
    },
    
    
    submitHandler: function(form) {
      form.submit();
    }
   });
