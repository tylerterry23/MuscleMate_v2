// AJAX Setup for CSRF token
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

// CSRF Token setup
var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

// Refresh table function
function refreshTable() {
    $.ajax({
        type: 'POST',
        url: 'refresh_table/',  // You'll have to set up this route in Django
        data: {
            'viewDate': $('#viewDate').val(),
            'workout': $('#workout').val(),
            'exercise': $('#exercise').val(),
            'filter': $('#filter').val(),
        },
        success: function (data) {
            $('#workout-log-table').html(data);
        },
    });
}

// Event listener on filter changes
$('#viewDate, #workout, #exercise, #filter').on('change', function () {
    refreshTable();
});

// Delete workout function
function deleteWorkout(id) {
    var conf = confirm("Are you sure you want to delete this workout?");
    if (conf == true) {
        $.ajax({
            type: "POST",
            url: "delete_workout/",  // You'll have to set up this route in Django
            data: {id: id},
            success: function(data) {
                refreshTable();
            }
        });
    }
}
