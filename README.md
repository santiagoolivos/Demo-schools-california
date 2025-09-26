# Demo Schools California

Una página web HTML simple con Tailwind CSS que muestra información sobre escuelas de California.

## 🎨 Características

- **HTML puro** con Tailwind CSS via CDN
- Título: "Demo Schools California" con gradiente moderno
- Botón Submit centrado (sin funcionalidad por el momento)
- Diseño responsive y moderno
- Efectos hover y animaciones
- Colores inspirados en California (azul y dorado)

## 🚀 Cómo ejecutar

### Opción 1: Abrir directamente
Simplemente abre el archivo `index.html` en tu navegador web.

### Opción 2: Servidor local
Para mejor experiencia de desarrollo, ejecuta un servidor local:

```bash
cd demo-schools-california

# Con Python
python3 -m http.server 3000

# Con Node.js (si tienes live-server)
npx live-server --port=3000

# Con PHP (si lo tienes instalado)
php -S localhost:3000
```

Luego abre: `http://localhost:3000`

## 📁 Estructura del proyecto

```
demo-schools-california/
├── index.html          # Página principal con HTML y Tailwind
└── README.md          # Este archivo
```

## 🎨 Diseño y estilos

- **Tailwind CSS** via CDN para estilos modernos
- Gradientes personalizados con colores de California
- Diseño responsive (mobile-first)
- Efectos hover y focus accesibles
- Animaciones suaves con CSS transitions
- Sombras y bordes redondeados modernos

## 🛠️ Tecnologías utilizadas

- **HTML5**
- **Tailwind CSS 3.x** (via CDN)
- **JavaScript** para interactividad básica
- Colores personalizados: `california-blue` y `california-gold`

## ✨ Funcionalidades

- Botón Submit con efecto visual al hacer clic
- Responsive design para móviles y desktop
- Animaciones de pulso decorativas
- Consola log cuando se hace clic en Submit

## 🔧 Personalización

El archivo incluye configuración personalizada de Tailwind:

```javascript
tailwind.config = {
    theme: {
        extend: {
            colors: {
                'california-blue': '#1e40af',
                'california-gold': '#f59e0b',
            }
        }
    }
}
```

## 📝 Próximos pasos

El botón Submit está listo para ser conectado con la funcionalidad específica que necesites implementar.
