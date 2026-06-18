import type {ClientModule} from '@docusaurus/types';

// Declare global variables for TypeScript
declare global {
  interface Window {
    fbq: any;
    gtag: any;
    trackLead: (channel: string) => void;
  }
}

// Function to track unified lead event
export function trackLead(channel: string) {
  const pagePath = window.location.pathname;
  const category = `${channel}${pagePath}`; // E.g., "line/es-k70/intro" or "line/catalog"

  console.log(`[Tracking] trackLead called for channel: ${channel}, path: ${pagePath}, category: ${category}`);

  // 1. Meta Pixel Lead (both pixels)
  if (typeof window.fbq === 'function') {
    window.fbq('track', 'Lead', {
      content_category: category,
      content_name: channel,
    });
  } else {
    console.warn('[Tracking] fbq is not defined');
  }

  // 2. GA4 generate_lead
  if (typeof window.gtag === 'function') {
    window.gtag('event', 'generate_lead', {
      channel: channel,
      page_path: pagePath,
      content_category: category,
    });
  } else {
    console.warn('[Tracking] gtag is not defined');
  }

  // 3. Google Ads Conversion
  if (typeof window.gtag === 'function') {
    window.gtag('event', 'conversion', {
      send_to: 'AW-958250070/6iosCJSI-b0cENb49sgD',
    });
  }
}

// Initialize global click listener and expose trackLead
if (typeof window !== 'undefined') {
  window.trackLead = trackLead;

  // Intercept click events on contact buttons/links
  document.addEventListener('click', (event) => {
    const target = event.target as HTMLElement;
    const anchor = target.closest('a');
    if (anchor && anchor.href) {
      let channel = '';
      const href = anchor.href.toLowerCase();
      
      if (href.includes('line.me')) {
        channel = 'line';
      } else if (href.includes('fb.com') || href.includes('facebook.com')) {
        channel = 'facebook';
      } else if (href.startsWith('mailto:') || href.includes('hello@mssiv.com')) {
        channel = 'email';
      }

      if (channel) {
        trackLead(channel);
      }
    }
  });
}

const trackingModule: ClientModule = {
  onRouteDidUpdate({location, previousLocation}) {
    // 1. Fire PageView on every route change
    if (typeof window.fbq === 'function') {
      window.fbq('track', 'PageView');
    }

    if (typeof window.gtag === 'function') {
      window.gtag('event', 'page_view', {
        page_path: location.pathname + location.search,
        page_title: document.title,
      });
    }

    // 2. Fire ViewContent specifically on ES-F501H page
    // Path could be /es-f501d or /en/es-f501d (and their subpages like /es-f501d/intro, etc.)
    const isF501dPage = /^\/(en\/)?es-f501d/i.test(location.pathname);
    if (isF501dPage) {
      console.log('[Tracking] Matching ES-F501H page, firing ViewContent');
      if (typeof window.fbq === 'function') {
        window.fbq('track', 'ViewContent', {
          content_name: 'ES-F501H',
          content_type: 'product',
          value: 10900,
          currency: 'THB',
        });
      }
    }
  },
};

export default trackingModule;
