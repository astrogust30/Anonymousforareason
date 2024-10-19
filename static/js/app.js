// app.js

$(document).ready(function() {
    // Create Rule Form Submission
    $('#create-rule-form').submit(function(event) {
        event.preventDefault();
        var name = $('#name').val();
        var rule_string = $('#rule_string').val();
        $.ajax({
            url: '/api/rules',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({name: name, rule_string: rule_string}),
            success: function(data) {
                showAlert('success', data.message || 'Rule created successfully.');
                setTimeout(function() {
                    location.reload();
                }, 1000);
            },
            error: function(xhr) {
                var error = xhr.responseJSON ? xhr.responseJSON.error : 'An error occurred.';
                showAlert('danger', error);
            }
        });
    });

    // Combine Rules Form Submission
    $('#combine-rules-form').submit(function(event) {
        event.preventDefault();
        var rule_names = $('#rule_names').val().split(',').map(s => s.trim());
        $.ajax({
            url: '/api/rules/combine',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({rule_names: rule_names}),
            success: function(data) {
                if (data.ast_json) {
                    $('#ast_json').val(JSON.stringify(data.ast_json, null, 2));
                    showAlert('success', 'Rules combined successfully.');
                } else {
                    showAlert('danger', data.error || 'Failed to combine rules.');
                }
            },
            error: function(xhr) {
                var error = xhr.responseJSON ? xhr.responseJSON.error : 'An error occurred.';
                showAlert('danger', error);
            }
        });
    });

    // Evaluate Rule Form Submission
    $('#evaluate-rule-form').submit(function(event) {
        event.preventDefault();
        var ast_json_text = $('#ast_json').val();
        var user_data_text = $('#user_data').val();
        var ast_json, user_data;
        try {
            ast_json = JSON.parse(ast_json_text);
            user_data = JSON.parse(user_data_text);
        } catch (e) {
            showAlert('danger', 'Invalid JSON input.');
            return;
        }
        $.ajax({
            url: '/api/evaluate',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ast_json: ast_json, user_data: user_data}),
            success: function(data) {
                if (data.eligible !== undefined) {
                    var resultText = data.eligible ? 'Eligible: Yes' : 'Eligible: No';
                    $('#result').html('<div class="alert alert-info">' + resultText + '</div>');
                } else {
                    showAlert('danger', data.error || 'Failed to evaluate rule.');
                }
            },
            error: function(xhr) {
                var error = xhr.responseJSON ? xhr.responseJSON.error : 'An error occurred.';
                showAlert('danger', error);
            }
        });
    });

    // Function to display alerts
    function showAlert(type, message) {
        var alertHtml = '<div class="alert alert-' + type + ' alert-dismissible fade show" role="alert">' +
                        message +
                        '<button type="button" class="close" data-dismiss="alert" aria-label="Close">' +
                        '<span aria-hidden="true">&times;</span>' +
                        '</button>' +
                        '</div>';
        $('body').prepend(alertHtml);
        // Auto-dismiss after 5 seconds
        setTimeout(function() {
            $('.alert').alert('close');
        }, 5000);
    }
});