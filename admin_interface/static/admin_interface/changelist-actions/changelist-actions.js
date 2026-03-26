(function() {
    'use strict';

    function toggleActions() {
        var actions = document.querySelector('#changelist .actions');
        if (!actions) return;
        var checked = document.querySelectorAll('#result_list input[type="checkbox"]:checked');
        if (checked.length > 0) {
            actions.classList.add('show');
        } else {
            actions.classList.remove('show');
        }
    }

    document.addEventListener('DOMContentLoaded', function() {
        var resultList = document.getElementById('result_list');
        if (!resultList) return;

        // Also handle the "select all" checkbox in thead
        var form = document.getElementById('changelist-form');
        if (form) {
            form.addEventListener('change', function(e) {
                if (e.target.type === 'checkbox') {
                    toggleActions();
                }
            });
        }

        // Initial state
        toggleActions();
    });
})();
