$(document).ready(function() {


    $('#calendar').fullCalendar({
        // put your options and callbacks here
        header:{
            left: 'prev,next',
            center: 'title',
            right: 'month,listMonth'

        },
        width: "100%",
        editable: false,
        themeSystem: 'standard',
        
        eventSources:[
            {
                url: 'https://google.com',
                type: 'POST',
                error: function() {
                    alert('Error encontrando eventos');
                },
            }
        ]
    })

});