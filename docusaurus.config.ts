import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'คู่มือการใช้งาน EPIC',
  tagline: 'คู่มือ EPIC ทุกรุ่น — อ่านออนไลน์ ภาษาไทย/อังกฤษ',
  favicon: 'img/favicon.ico',

  future: {
    v4: true,
  },

  // Production URL — Cloudflare Pages custom domain
  url: 'https://manual.mssiv.com',
  baseUrl: '/',

  trailingSlash: false,

  organizationName: 'mssiv',
  projectName: 'manual-mssiv',

  onBrokenLinks: 'warn',

  // TH default (ลูกค้าไทย), EN secondary
  i18n: {
    defaultLocale: 'th',
    locales: ['th', 'en'],
    localeConfigs: {
      th: {
        label: 'ภาษาไทย',
        direction: 'ltr',
        htmlLang: 'th-TH',
      },
      en: {
        label: 'English',
        direction: 'ltr',
        htmlLang: 'en-US',
      },
    },
  },

  presets: [
    [
      'classic',
      {
        docs: {
          path: 'docs', // TH default locale
          routeBasePath: '/', // clean URLs: /, /es-k70/intro, /catalog
          sidebarPath: './sidebars.ts',
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
    docs: {
      sidebar: {
        autoCollapseCategories: true,
      },
    },
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
        {to: '/catalog', label: 'คู่มือทั้งหมด', position: 'left'},
        {
          type: 'localeDropdown',
          position: 'right',
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
          title: 'EPIC Manuals',
          items: [
            {label: 'คู่มือทั้งหมด', to: '/catalog'},
            {label: 'English Version', to: '/en/catalog'},
          ],
        },
        {
          title: 'EPIC',
          items: [
            {label: 'เว็บไซต์ทางการ', href: 'https://www.epic.co.kr'},
            {label: 'epicdoorlock.com', href: 'https://epicdoorlock.com'},
            {label: 'LINE @epicdoorlock', href: 'https://line.me/R/ti/p/@epicdoorlock'},
            {label: 'Facebook', href: 'https://fb.com/epicdoorlock'},
          ],
        },
      ],
      copyright: `Copyright © 2026 Massive System Co.,Ltd. Built with Docusaurus.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
