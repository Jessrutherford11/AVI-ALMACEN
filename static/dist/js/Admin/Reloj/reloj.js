    
      var udateTime = function () {
        let currentDate = new Date(),
          hours = currentDate.getHours(),
          minutes = currentDate.getMinutes(),
          seconds = currentDate.getSeconds(),
          weekDay = currentDate.getDay(),
          day = currentDate.getDate(),
          month = currentDate.getMonth(),
          year = currentDate.getFullYear();
        console.log(day);
        const dias = [
          'Domingo',
          'Lunes',
          'Martes',
          'Miércoles',
          'Jueves',
          'Viernes',
          'Sabado'
        ];
        const meses = [
          'Enero',
          'Febrero',
          'Marzo',
          'Abril',
          'Mayo',
          'Junio',
          'Julio',
          'Agosto',
          'Septiembre',
          'Octubre',
          'Noviembre',
          'Diciembre'
        ];

        if (minutes < 10) {
          minutes = "0" + minutes
        }

        if (seconds < 10) {
          seconds = "0" + seconds
        }


        var fecha = `${dias[weekDay]} ${day} de ${meses[month]}`;
        var hora = `${hours} : ${minutes} : ${seconds} HRS`;



        document.getElementById('fecha').textContent = fecha;
        document.getElementById('hora').textContent = hora;
      };

      udateTime();
      setInterval(udateTime, 1000);
    