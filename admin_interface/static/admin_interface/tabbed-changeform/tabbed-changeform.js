(function (AdminInterface) {

    var scope = AdminInterface;

    scope.tabbedChangeForm = {

        hightlightTabsWithErrors: function() {
            document.querySelectorAll(".errorlist").forEach((el) => {
                const tabContent = el.closest(".tabbed-changeform-tabcontent");
                if (tabContent) {
                    const tabName = tabContent.id.replace("tabcontent-", "");
                    const tabEl = document.getElementById("tablink-" + tabName);
                    if (tabEl) {
                        tabEl.classList.add("error");
                    }
                }
            });
        },

        openFirstErrorTab: function() {
            // After a failed save, land the operator on the tab that actually
            // holds the error instead of a clean-looking active tab.
            var active = document.querySelector(".tabbed-changeform-tablink.active");
            if (active && active.classList.contains("error")) {
                return;
            }
            var firstError = document.querySelector(".tabbed-changeform-tablink.error");
            if (firstError) {
                var tabName = firstError.id.replace("tablink-", "");
                this.openTabByName(tabName);
                this.scrollTabsToTabByName(tabName);
            }
        },

        openTab: function (event, tabName) {
            this.openTabByName(tabName);
        },

        openTabByName: function(tabName) {
            let tablinkEl = document.getElementById("tablink-" + tabName);
            let tabcontentEl = document.getElementById("tabcontent-" + tabName);
            if (!tablinkEl || !tabcontentEl) {
                return false;
            }

            let tablinks = document.getElementsByClassName("tabbed-changeform-tablink");
            let tabcontents = document.getElementsByClassName("tabbed-changeform-tabcontent");

            // toggle tab link
            for (let tablink of tablinks) {
                tablink.classList.remove("active");
            }
            tablinkEl.classList.add("active");

            // toggle tab content
            for (let tabcontent of tabcontents) {
                tabcontent.classList.remove("active");
            }
            tabcontentEl.classList.add("active");

            // update location hash
            let history = window.history;
            if (history) {
                history.replaceState(undefined, undefined, "#" + tabName);
            }

            return true;
        },

        openTabByLocationHash: function() {
            let hash = window.location.hash;
            if (hash && hash !== "#") {
                let tabName = hash.substring(1);
                if (this.openTabByName(tabName)) {
                    this.scrollTabsToTabByName(tabName);
                }
            }
        },

        scrollTabsToTabByName: function(tabName) {
            let tabsEl = document.getElementById("tabbed-changeform-tabs");
            let tablinkEl = document.getElementById("tablink-" + tabName);
            if (!tabsEl || !tablinkEl) {
                return;
            }
            let tablinkLeft = (tablinkEl.offsetLeft - tabsEl.offsetLeft);
            let tabsScrollLeft = Math.ceil(tablinkLeft);
            tabsEl.scrollTo({
                top: 0,
                left: tabsScrollLeft,
                behavior: "instant"
            });
        }
    };

    // scope.tabbedChangeForm.openTabByLocationHash();
    document.addEventListener('DOMContentLoaded', function() {
        scope.tabbedChangeForm.hightlightTabsWithErrors();
        scope.tabbedChangeForm.openTabByLocationHash();
        scope.tabbedChangeForm.openFirstErrorTab();
    }, false);

}(window.AdminInterface = window.AdminInterface || {}));
