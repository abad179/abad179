// Funciones de autenticación y roles
function detectarRol(email) {
  const lower = email.toLowerCase();
  if (lower.includes('admin') || lower.includes('director')) return 'ADMIN';
  if (lower.includes('@rioverde') || lower.includes('gob.mx') || lower.includes('supervisor') || lower.includes('municipio')) return 'SUPERVISOR';
  return 'CLIENTE';
}

function cargarSesion() {
  const sesion = localStorage.getItem('sesion');
  return sesion ? JSON.parse(sesion) : null;
}

function guardarSesion(data) {
  localStorage.setItem('sesion', JSON.stringify(data));
}

function cerrarSesion() {
  localStorage.removeItem('sesion');
  location.reload();
}

// Datos de espacios
let espacios = cargarEspacios();

function cargarEspacios() {
  const data = localStorage.getItem('espacios');
  if (data) return JSON.parse(data);
  return [
    { id: 1, coords: [-100.9, 21.93], x: 10, y: 10, estado: 'LIBRE', type: 'AUTO' },
    { id: 2, coords: [-100.905, 21.931], x: 60, y: 30, estado: 'ACTIVO', type: 'AUTO' }
  ];
}

function debounce(fn, delay) {
  let t;
  return function () {
    clearTimeout(t);
    t = setTimeout(fn, delay);
  };
}

const guardarEspaciosDebounced = debounce(() => {
  localStorage.setItem('espacios', JSON.stringify(espacios));
}, 500);

function colorPorEstado(estado) {
  switch (estado) {
    case 'POR VENCER':
      return 'orange';
    case 'VENCIDO':
      return 'red';
    case 'ACTIVO':
    case 'LIBRE':
    default:
      return 'green';
  }
}

function actualizarMetricas() {
  const total = espacios.length;
  const libres = espacios.filter(e => e.estado === 'LIBRE').length;
  const activos = espacios.filter(e => e.estado === 'ACTIVO').length;
  document.getElementById('metricTotal').textContent = total;
  document.getElementById('metricFree').textContent = libres;
  document.getElementById('metricActive').textContent = activos;
}

// Inicialización de MapLibre simple
let map;
function initMap() {
  map = new maplibregl.Map({
    container: 'map',
    style: 'https://demotiles.maplibre.org/style.json',
    center: [-100.9, 21.93],
    zoom: 14
  });

  espacios.forEach(e => {
    new maplibregl.Marker({ color: colorPorEstado(e.estado) })
      .setLngLat(e.coords)
      .addTo(map)
      .getElement()
      .addEventListener('click', () => seleccionarEspacio(e.id));
  });
}

function renderCroquis() {
  const svg = document.getElementById('sketchSvg');
  svg.innerHTML = '';
  espacios.forEach(e => {
    const rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
    rect.setAttribute('x', e.x);
    rect.setAttribute('y', e.y);
    rect.setAttribute('width', 20);
    rect.setAttribute('height', 10);
    rect.setAttribute('fill', colorPorEstado(e.estado));
    rect.addEventListener('click', () => seleccionarEspacio(e.id));
    svg.appendChild(rect);
  });
}

let vista = 'MAPA';
function toggleView() {
  if (vista === 'MAPA') {
    document.getElementById('map').classList.add('hidden');
    document.getElementById('sketch').classList.remove('hidden');
    document.getElementById('toggleView').textContent = 'Mapa';
    vista = 'CROQUIS';
    renderCroquis();
  } else {
    document.getElementById('map').classList.remove('hidden');
    document.getElementById('sketch').classList.add('hidden');
    document.getElementById('toggleView').textContent = 'Croquis';
    vista = 'MAPA';
  }
}

let seleccionado = null;
function seleccionarEspacio(id) {
  seleccionado = espacios.find(e => e.id === id);
  console.log('Seleccionado', seleccionado);
}

// Render según rol
function mostrarApp(rol, nombre) {
  document.getElementById('auth').classList.add('hidden');
  document.getElementById('app').classList.remove('hidden');
  document.getElementById('roleTitle').textContent = `${rol}${nombre ? ' - ' + nombre : ''}`;
  initMap();
  actualizarMetricas();
  guardarEspaciosDebounced();
}

// Configurar formulario
const loginForm = document.getElementById('loginForm');
loginForm.addEventListener('submit', (e) => {
  e.preventDefault();
  const nombre = document.getElementById('name').value.trim();
  const email = document.getElementById('email').value.trim();
  const plate = document.getElementById('plate').value.trim();

  const rol = detectarRol(email);
  const sesion = { nombre, email, plate, rol };
  guardarSesion(sesion);
  mostrarApp(rol, nombre);
});

document.getElementById('logout').addEventListener('click', cerrarSesion);
document.getElementById('toggleView').addEventListener('click', toggleView);

// Revisar si hay sesión existente
const sesion = cargarSesion();
if (sesion) {
  mostrarApp(sesion.rol, sesion.nombre);
}
