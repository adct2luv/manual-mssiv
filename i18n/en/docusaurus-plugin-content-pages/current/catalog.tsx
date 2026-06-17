import type {ReactNode} from 'react';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';
import Link from '@docusaurus/Link';

type Manual = {
  title: string;
  slug: string;
  category: 'product' | 'guide' | 'app' | 'consolidated';
  size: string;
  image?: string;
  onlinePath?: string;
};

const PRODUCT_MANUALS: Manual[] = [
  {title: 'EF-8000L', slug: 'ef-8000l', category: 'product', size: '5.5 MB'},
  {title: 'EF-P8800K', slug: 'ef-p8800k', category: 'product', size: '3.7 MB', image: '/img/brochures/ef-p8800k.png'},
  {title: 'ES-303G', slug: 'es-303g', category: 'product', size: '3.8 MB', image: '/img/brochures/es-303g.png'},
  {title: 'ES-809L', slug: 'es-809l', category: 'product', size: '6.5 MB'},
  {title: 'ES-B10', slug: 'es-b10', category: 'product', size: '14 MB', image: '/img/brochures/es-b10.png'},
  {title: 'ES-K70', slug: 'es-k70', category: 'product', size: '8.2 MB', onlinePath: '/es-k70/intro'},
  {title: 'ES-L200 Series', slug: 'es-l200', category: 'product', size: '252 KB', image: '/img/brochures/es-l200.png'},
  {title: 'ES-M50', slug: 'es-m50', category: 'product', size: '3.1 MB', image: '/img/brochures/es-m50.png'},
  {title: 'ES-P9100FK', slug: 'es-p9100fk', category: 'product', size: '10 MB'},
  {title: 'ES-T153', slug: 'es-t153', category: 'product', size: '20 MB'},
  {title: 'N-TOUCH', slug: 'n-touch', category: 'product', size: '5.9 MB', image: '/img/brochures/n-touch.png'},
  {title: 'OS300H', slug: 'os300h', category: 'product', size: '0.8 MB', image: '/img/brochures/os300h.png'},
  {title: 'POPscan', slug: 'popscan', category: 'product', size: '12 MB', image: '/img/brochures/popscan.png'},
  {title: 'TOUCH', slug: 'touch', category: 'product', size: '13 MB', image: '/img/brochures/touch.png'},
  {title: 'TRIPLEX 2way', slug: 'triplex-2way', category: 'product', size: '14 MB'},
  {title: 'TRIPLEX 3way', slug: 'triplex-3way', category: 'product', size: '17 MB'},
];

const REFERENCE_GUIDES: Manual[] = [
  {title: 'Key Tail Assembly Guide', slug: 'key-tail-assembly', category: 'guide', size: '0.4 MB'},
  {title: 'Consolidated Manual (Rev.09)', slug: 'consolidated-manual', category: 'consolidated', size: '5.7 MB'},
  {title: 'IR Sensor Usage Guide for Face ID', slug: 'ir-sensor-face-id', category: 'guide', size: '0.5 MB'},
  {title: 'Outer Body Cable Management Guide', slug: 'outer-body-cable', category: 'guide', size: '0.1 MB'},
  {title: 'Remote Control Compatibility', slug: 'remote-control-compat', category: 'guide', size: '0.1 MB'},
];

const APP_MANUALS: Manual[] = [
  {title: 'EPIC Things APP', slug: 'epic-things-app', category: 'app', size: '9.4 MB'},
];

function ManualCard({m}: {m: Manual}) {
  return (
    <div className="col col--4 margin-bottom--lg">
      <div className="manual-card">
        {m.image && (
          <img
            src={m.image}
            alt={m.title}
            style={{width: '100%', height: '180px', objectFit: 'contain', marginBottom: '0.75rem', background: '#fafafa'}}
          />
        )}
        <div>
          <h3 className="manual-card__title">{m.title}</h3>
          <p className="manual-card__meta">{m.size} · {m.category}</p>
        </div>
      </div>
    </div>
  );
}

function ManualGrid({manuals, title, description}: {manuals: Manual[]; title: string; description?: string}) {
  return (
    <section className="margin-top--lg">
      <Heading as="h2">{title} ({manuals.length})</Heading>
      {description && <p>{description}</p>}
      <div className="row">
        {manuals.map((m) => (
          <ManualCard key={m.slug} m={m} />
        ))}
      </div>
    </section>
  );
}

export default function Catalog(): ReactNode {
  return (
    <Layout
      title="All manuals catalogue"
      description="Catalogue of all 22 EPIC manuals — products, references and apps"
    >
      <main className="container margin-vert--lg">
        <Heading as="h1">All manuals catalogue</Heading>
        <p>
          All <strong>{PRODUCT_MANUALS.length + REFERENCE_GUIDES.length + APP_MANUALS.length} manuals</strong> from <a href="https://www.epic.co.kr/home/manual/" target="_blank" rel="noopener noreferrer">epic.co.kr/home/manual/</a>
          {' '}— refreshed 2026-06-16
        </p>

        <ManualGrid
          manuals={PRODUCT_MANUALS}
          title="Product manuals"
          description="User manuals for each EPIC door lock model"
        />
        <ManualGrid
          manuals={REFERENCE_GUIDES}
          title="Installation & reference guides"
          description="Cross-model installation and compatibility guides"
        />
        <ManualGrid
          manuals={APP_MANUALS}
          title="Apps & software"
        />

        <p className="margin-top--xl">
          <small>
            Note: Currently only <strong>ES-K70</strong> has a full online manual. More models are coming soon — see <Link to="/es-k70/intro">the ES-K70 example</Link>.
          </small>
        </p>
      </main>
    </Layout>
  );
}
