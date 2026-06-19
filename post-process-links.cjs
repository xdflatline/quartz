const fs = require('fs');
const path = require('path');

const PUBLIC_DIR = path.join(__dirname, 'public');

// Extensions that should NOT have .html added
const KNOWN_EXTENSIONS = [
  '.html', '.css', '.js', '.png', '.webp', '.jpg', '.jpeg', '.gif',
  '.svg', '.woff', '.woff2', '.ttf', '.eot', '.json', '.xml',
  '.ico', '.pdf', '.txt', '.md', '.map', '.wasm',
  '.mp4', '.webm', '.ogg', '.mp3', '.wav', '.avi', '.mov'
];

function shouldAddHtmlExt(href) {
  // Skip external links, anchors, mailto, javascript:, data:, etc.
  if (href.startsWith('http://') || href.startsWith('https://') ||
      href.startsWith('//') || href.startsWith('#') ||
      href.startsWith('mailto:') || href.startsWith('tel:') ||
      href.startsWith('javascript:') || href.startsWith('data:') ||
      href.startsWith('blob:')) {
    return false;
  }

  // Skip if it already has a known extension
  const lowerHref = href.toLowerCase();
  for (const ext of KNOWN_EXTENSIONS) {
    if (lowerHref.endsWith(ext)) {
      return false;
    }
  }

  // Skip if it ends with / (folder path - will use index.html)
  if (href.endsWith('/')) {
    return false;
  }

  // Skip empty or just "."
  if (!href || href === '.' || href === './') {
    return false;
  }

  // Skip pure directory traversal paths (.., ../.., ../../.., etc.)
  // These are relative paths that don't point to a specific file
  if (/^(\.\.\/)+$/.test(href) || href === '..' || /^(\.\.\/)*\.\.$/.test(href)) {
    return false;
  }

  // Skip paths that are just ./.. or ../.. etc. (traversal without a file)
  if (/^(\.\/)?(\.\.\/)*\.\.?$/.test(href)) {
    return false;
  }

  return true;
}

function processHtmlFile(filePath) {
  let content = fs.readFileSync(filePath, 'utf-8');
  let changed = false;

  // Replace href attributes in <a> tags
  content = content.replace(/href="([^"]*)"/g, (match, href) => {
    if (shouldAddHtmlExt(href)) {
      changed = true;
      return `href="${href}.html"`;
    }
    return match;
  });

  if (changed) {
    fs.writeFileSync(filePath, content, 'utf-8');
    console.log(`Updated: ${filePath}`);
  }
}

// Walk all HTML files
function walk(dir) {
  const files = fs.readdirSync(dir);
  for (const file of files) {
    const fullPath = path.join(dir, file);
    const stat = fs.statSync(fullPath);
    if (stat.isDirectory()) {
      walk(fullPath);
    } else if (file.endsWith('.html')) {
      processHtmlFile(fullPath);
    }
  }
}

console.log('Post-processing HTML links for GitHub Pages...');
walk(PUBLIC_DIR);
console.log('Done!');
