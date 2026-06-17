import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  esK70Sidebar: [
    'es-k70/intro',
    {
      type: 'category',
      label: 'Getting Started',
      collapsed: false,
      items: [
        'es-k70/safety',
        'es-k70/specs',
        'es-k70/components',
      ],
    },
    {
      type: 'category',
      label: 'Programming',
      collapsed: false,
      items: [
        'es-k70/pin-registration',
        'es-k70/rfid-registration',
        'es-k70/rfid-deletion',
      ],
    },
  ],
};

export default sidebars;
