module.exports = {
  future: {
      removeDeprecatedGapUtilities: true,
      purgeLayersByDefault: true,
  },
  mode : 'jit',
  content: {
      enabled: false, //true for production build
      content: [
          '../**/templates/*.html',
          '../**/templates/**/*.html',
      ]
  },
  theme: {
      extend: {
        colors: {
        primary:'#3D3B40',
        secondary: {
          100: '#E84545',
          200:'#903749',
          300:'#53354A',
          400:'#FFA559',
          500:'#FF6000',
          600:'#C0FEFC',
          700:'#046832',
          800: '#E5E5CB',
          900:'#FFE6C7',
          
        },
        primary2:'#454545',
        puerto_rico: {
          '50': '#effefa',
          '100': '#cafdf2',
          '200': '#94fbe8',
          '300': '#57f1db',
          '400': '#25dcc7',
          '500': '#0cc0ae',
          '600': '#069b8e',
          '700': '#0a7b73',
          '800': '#0d625d',
          '900': '#10514d',
          '950': '#023130',
      },
      sepia_black: {
        '50': '#fff0f0',
        '100': '#ffdddd',
        '200': '#ffc1c1',
        '300': '#ff9696',
        '400': '#ff5a5a',
        '500': '#ff2727',
        '600': '#fb0707',
        '700': '#d40101',
        '800': '#ae0606',
        '900': '#900c0c',
        '950': '#290000',
    },
    
      
      },
      fontFamily:{
        body:['Chivo'],
        secondary:['Evo']
      },
      width:{
        800 : '800px'
      },
    },
  },
  variants: {},
  plugins: [],
}
