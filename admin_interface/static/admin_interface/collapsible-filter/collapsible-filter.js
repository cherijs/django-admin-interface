(function() {
    var STORAGE_KEY = 'admin-interface.list-filter-collapsed';

    function init() {
        var filterEl = document.getElementById('changelist-filter');
        if (!filterEl) {
            return;
        }

        var headerEl = filterEl.querySelector('h2');
        if (!headerEl) {
            return;
        }

        // Apply saved state
        var collapsed = localStorage.getItem(STORAGE_KEY) === '1';
        if (collapsed) {
            filterEl.classList.add('collapsed');
        }

        // Make header clickable
        headerEl.style.cursor = 'pointer';

        headerEl.addEventListener('click', function() {
            filterEl.classList.toggle('collapsed');
            var isCollapsed = filterEl.classList.contains('collapsed');
            localStorage.setItem(STORAGE_KEY, isCollapsed ? '1' : '0');
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
