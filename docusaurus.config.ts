import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'EPIC Manuals',
  tagline: 'Official product manuals, online',
  favicon: 'img/favicon.ico',

  future: {
    v4: true,
  },

  // Production URL — set after first deploy once the custom domain is attached.
  url: 'https://manual.mssiv.com',
  baseUrl: '/',

  // Trailing-slash policy for clean URLs on Cloudflare Pages.
  trailingSlash: false,

  organizationName: 'mssiv',
  projectName: 'manual-mssiv',

  onBrokenLinks: 'throw',

  markdown: {
    hooks: {
      onBrokenMarkdownLinks: 'warn',
    },
  },

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          routeBasePath: '/manuals',
          showLastUpdateTime: false,
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    colorMode: {
      defaultMode: 'light',
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: 'EPIC Manuals',
      logo: {
        alt: 'EPIC',
        src: 'img/epic-logo.svg',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'esK70Sidebar',
          position: 'left',
          label: 'ES-K70',
        },
        {
          to: '/catalog',
          label: 'All Manuals',
          position: 'left',
        },
        {
          href: 'https://epicdoorlock.com',
          label: 'epicdoorlock.com ↗',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Manuals',
          items: [
            {label: 'ES-K70 Online', to: '/manuals/es-k70/intro'},
            {label: 'All Manuals (PDF)', to: '/catalog'},
          ],
        },
        {
          title: 'EPIC',
          items: [
            {label: 'Official Site', href: 'https://www.epic.co.kr'},
            {label: 'epicdoorlock.com', href: 'https://epicdoorlock.com'},
            {label: 'LINE @epicdoorlock', href: 'https://line.me/R/ti/p/@epicdoorlock'},
            {label: 'Facebook', href: 'https://fb.com/epicdoorlock'},
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} EPIC Door Lock. Built with Docusaurus.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
      additionalLanguages: ['bash'],
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
