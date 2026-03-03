/** global: django */

if (typeof(django) !== 'undefined' && typeof(django.jQuery) !== 'undefined')
{
    (function($) {

        $(document).ready(function(){

            function collapsibleInline(scope, collapsed) {
                var fieldsetCollapsed = collapsed;
                var fieldsetEl = $(scope).find('> fieldset.module');
                fieldsetEl.addClass('collapse');
                var fieldsetHasErrors = (fieldsetEl.children('.errors').length > 0);
                if (fieldsetHasErrors === true) {
                    fieldsetCollapsed = false;
                }
                if (fieldsetCollapsed === true) {
                    fieldsetEl.addClass('collapsed');
                }
                var collapseToggleText = (fieldsetCollapsed ? gettext('Show') : gettext('Hide'));
                var collapseToggleHTML = ' (<a class="collapse-toggle" href="#">' + collapseToggleText + '</a>)';
                var headerEl = fieldsetEl.find('> h2,> h3');
                if (headerEl.find(".collapse-toggle").length === 0) {
                    headerEl.append(collapseToggleHTML);
                }
                headerEl.find('.collapse-toggle').on('click', function(e) {
                    e.preventDefault();
                    if (fieldsetEl.hasClass('collapsed')) {
                        fieldsetEl.removeClass('collapsed');
                        $(this).text(gettext('Hide'));
                    } else {
                        fieldsetEl.addClass('collapsed');
                        $(this).text(gettext('Show'));
                    }
                });
            }

            var stackedInlinesOptionSel = '.admin-interface.collapsible-stacked-inlines';
            var stackedInlinesSel = stackedInlinesOptionSel + ' .inline-group[data-inline-type="stacked"]';
            var stackedInlinesCollapsed = $(stackedInlinesOptionSel).hasClass('collapsible-stacked-inlines-collapsed');

            var tabularInlinesOptionSel = '.admin-interface.collapsible-tabular-inlines';
            var tabularInlinesSel = tabularInlinesOptionSel + ' .inline-group[data-inline-type="tabular"] .inline-related.tabular';
            var tabularInlinesCollapsed = $(tabularInlinesOptionSel).hasClass('collapsible-tabular-inlines-collapsed');

            $(stackedInlinesSel).each(function() {
                collapsibleInline(this, stackedInlinesCollapsed);
            });

            $(tabularInlinesSel).each(function() {
                collapsibleInline(this, tabularInlinesCollapsed);
            });

        });

    })(django.jQuery);
}
