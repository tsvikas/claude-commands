// Sorts the cards into columns, opens a row on press, filters, opens everything at once, and switches the theme.
(() => {
  const root = document.documentElement;
  root.classList.remove("no-js");

  const board = document.getElementById("board");
  const secs = [...board.querySelectorAll(".sec")];
  const groups = [...board.querySelectorAll(".grp")];
  const rows = [...board.querySelectorAll(".row")];
  const GAP = 16;
  const MIN_COLUMN = 290;
  const MAX_COLUMNS = 5;
  let columns = 0;

  // As many columns as fit, the cards in reading order, the tallest column as short as it can be.
  // It runs when the column count changes, never when a row opens, so a press does not move a card.
  function layout(force) {
    const fit = Math.floor((board.clientWidth + GAP) / (MIN_COLUMN + GAP));
    const n = Math.max(1, Math.min(MAX_COLUMNS, fit));
    if (n === columns && !force) return;
    columns = n;
    board.style.setProperty("--cols", n);

    const probe = document.createElement("div");
    probe.className = "col";
    probe.append(...secs);
    board.replaceChildren(probe);
    const shown = secs.filter((sec) => !sec.hidden);
    const heights = shown.map((sec) => sec.offsetHeight + GAP);

    const fits = (cap) => {
      let used = 1;
      let height = 0;
      for (const h of heights) {
        if (height + h > cap) {
          used += 1;
          height = 0;
        }
        height += h;
      }
      return used <= n;
    };
    let low = Math.max(0, ...heights);
    let high = heights.reduce((a, b) => a + b, 0);
    while (low < high) {
      const mid = Math.floor((low + high) / 2);
      if (fits(mid)) high = mid;
      else low = mid + 1;
    }

    const cols = [];
    let height = 0;
    shown.forEach((sec, i) => {
      if (!cols.length || height + heights[i] > low) {
        cols.push(document.createElement("div"));
        height = 0;
      }
      cols.at(-1).append(sec);
      height += heights[i];
    });
    cols.forEach((col, i) => {
      const side = n === 1 ? "tip-below" : i > 0 && i === n - 1 ? "tip-left" : "tip-right";
      col.className = `col ${side}`;
    });
    board.replaceChildren(...cols);
  }

  function setOpen(row, open) {
    row.classList.toggle("open", open);
    row.querySelector("button.name").setAttribute("aria-expanded", open);
  }

  board.addEventListener("click", (event) => {
    const row = event.target.closest(".row.can");
    // a press that ends a text selection is not a press on the row
    if (!row || String(getSelection())) return;
    setOpen(row, !row.classList.contains("open"));
  });

  const all = document.getElementById("all");
  all.addEventListener("click", () => {
    const open = all.getAttribute("aria-pressed") !== "true";
    all.setAttribute("aria-pressed", open);
    all.textContent = open ? "Collapse details" : "Expand all details";
    for (const row of rows) if (row.classList.contains("can")) setOpen(row, open);
    layout(true);
  });

  // The page follows the system until the toggle is pressed; then the choice is kept in this browser.
  // The script in the head applies a kept choice before the first paint.
  const theme = document.getElementById("theme");
  const system = matchMedia("(prefers-color-scheme: dark)");
  const isDark = () => (root.dataset.theme ? root.dataset.theme === "dark" : system.matches);
  const label = () => (theme.textContent = isDark() ? "Light theme" : "Dark theme");
  theme.addEventListener("click", () => {
    root.dataset.theme = isDark() ? "light" : "dark";
    try {
      localStorage.setItem("theme", root.dataset.theme);
    } catch {
      // a private window may refuse; the choice then lasts until the page is closed
    }
    label();
  });
  system.addEventListener("change", label);
  label();

  // A filter shows the matching rows whole, and hides the sentences that belong to no row.
  const query = document.getElementById("q");
  const empty = document.getElementById("empty");
  query.addEventListener("input", () => {
    const text = query.value.trim().toLowerCase();
    root.classList.toggle("filtering", text !== "");
    for (const row of rows) row.hidden = text !== "" && !row.dataset.text.includes(text);
    for (const part of [...groups, ...secs]) part.hidden = !part.querySelector(".row:not([hidden])");
    empty.hidden = secs.some((sec) => !sec.hidden);
    layout(true);
  });

  new ResizeObserver(() => layout()).observe(board);
  layout();
  // the web font changes the heights the first layout measured
  document.fonts?.ready.then(() => layout(true));
})();
