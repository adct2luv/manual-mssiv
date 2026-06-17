import type {ReactNode} from 'react';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';
import Link from '@docusaurus/Link';

type Manual = {
  title: string;
  file: string;
  size: string;
  category: 'product' | 'reference' | 'app';
  /** If set, link to the full online manual instead of / being a PDF */
  onlinePath?: string;
};

const PRODUCT_MANUALS: Manual[] = [
  {title: 'EF-8000L',     file: 'Manual_EF-8000L.pdf',     size: '5.5 MB', category: 'product'},
  {title: 'EF-P8800K',    file: 'Manual_EF-P8800K.pdf',    size: '3.7 MB', category: 'product'},
  {title: 'ES-303G',      file: 'Manual_ES-303G.pdf',      size: '3.8 MB', category: 'product'},
  {title: 'ES-809L',      file: 'Manual_ES-809L.pdf',      size: '6.4 MB', category: 'product'},
  {title: 'ES-B10',       file: 'Manual_ES-B10.pdf',       size: '14 MB',  category: 'product'},
  {title: 'ES-K70',       file: 'Manual_ES-K70.pdf',       size: '8.2 MB', category: 'product', onlinePath: '/manuals/es-k70/intro'},
  {title: 'ES-L200 Series', file: 'Manual_ES-L200 Series.pdf', size: '252 KB', category: 'product'},
  {title: 'ES-M50',       file: 'Manual_ES-M50.pdf',       size: '3.1 MB', category: 'product'},
  {title: 'ES-P9100FK',   file: 'Manual_ES-P9100FK.pdf',   size: '10 MB',  category: 'product'},
  {title: 'ES-T153',      file: 'Manual_ES-T153.pdf',      size: '20 MB',  category: 'product'},
  {title: 'N-TOUCH',      file: 'Manual_N-TOUCH.pdf',      size: '5.9 MB', category: 'product'},
  {title: 'OS300H',       file: 'Manual_OS300H.pdf',       size: '0.8 MB', category: 'product'},
  {title: 'POPscan',      file: 'Manual_POPscan.pdf',      size: '12 MB',  category: 'product'},
  {title: 'TOUCH',        file: 'Manual_TOUCH.pdf',        size: '13 MB',  category: 'product'},
  {title: 'TRIPLEX 2way', file: 'Manual_TRIPLEX 2way.pdf', size: '14 MB',  category: 'product'},
  {title: 'TRIPLEX 3way', file: 'Manual_TRIPLEX 3way.pdf', size: '17 MB',  category: 'product'},
];

const REFERENCE_GUIDES: Manual[] = [
  {title: 'Assembly Guide for Key Tail',           file: 'Assembly Guide for Key Tail.pdf',           size: '0.4 MB', category: 'reference'},
  {title: 'Consolidated Manual (Rev.09)',          file: 'Consolidated-Manual-Rev.09.pdf',           size: '5.7 MB', category: 'reference'},
  {title: 'IR Sensor Usage Guide for Face ID',     file: 'IR Sensor Usage Guide for Face ID.pdf',    size: '0.5 MB', category: 'reference'},
  {title: 'Outer Body Cable Management Guide',     file: 'Outer Body Cable Management Guide.pdf',    size: '0.1 MB', category: 'reference'},
  {title: 'Remote-Control Module Compatibility',   file: 'Remote-Control-Module-Compatibility-Guide.pdf', size: '0.1 MB', category: 'reference'},
];

const APP_MANUALS: Manual[] = [
  {title: 'EPIC Things APP User Manual', file: 'EPIC Things APP User Manual.pdf', size: '9.4 MB', category: 'app'},
];

function pdfUrl(file: string): string {
  return `/manuals/${encodeURIComponent(file)}`;
}

function ManualCard({m}: {m: Manual}) {
  return (
    <div className="manual-card col col--4 margin-bottom--md">
      <div>
        <h3 className="manual-card__title">{m.title}</h3>
        <p className="manual-card__meta">PDF · {m.size}</p>
      </div>
      <div className="manual-card__actions">
        {m.onlinePath && (
          <Link className="button button--primary button--sm" to={m.onlinePath}>
            Read online
          </Link>
        )}
        <a
          className={`button button--sm ${m.onlinePath ? 'button--outline button--primary' : 'button--primary'}`}
          href={pdfUrl(m.file)}
          target="_blank"
          rel="noopener noreferrer"
        >
          Download PDF
        </a>
      </div>
    </div>
  );
}

function ManualGrid({manuals}: {manuals: Manual[]}) {
  return (
    <div className="row">
      {manuals.map((m) => (
        <ManualCard key={m.file} m={m} />
      ))}
    </div>
  );
}

export default function Catalog(): ReactNode {
  return (
    <Layout
      title="All Manuals"
      description="Complete catalog of EPIC product manuals, reference guides, and app documentation."
    >
      <header className="hero hero--primary">
        <div className="container">
          <Heading as="h1">All Manuals</Heading>
          <p>{PRODUCT_MANUALS.length + REFERENCE_GUIDES.length + APP_MANUALS.length} documents from epic.co.kr — PDF downloads, with one online edition.</p>
        </div>
      </header>
      <main className="container margin-vert--lg">
        <section>
          <Heading as="h2">Per-product manuals ({PRODUCT_MANUALS.length})</Heading>
          <p>Owner's manuals for individual EPIC door-lock models.</p>
          <ManualGrid manuals={PRODUCT_MANUALS} />
        </section>

        <section className="margin-top--xl">
          <Heading as="h2">Installation &amp; reference guides ({REFERENCE_GUIDES.length})</Heading>
          <p>Cross-product installation and compatibility references.</p>
          <ManualGrid manuals={REFERENCE_GUIDES} />
        </section>

        <section className="margin-top--xl">
          <Heading as="h2">Apps &amp; software ({APP_MANUALS.length})</Heading>
          <p>Companion-app documentation.</p>
          <ManualGrid manuals={APP_MANUALS} />
        </section>

        <section className="margin-top--xl">
          <p>
            <small>
              Source: <a href="https://www.epic.co.kr/home/manual/" target="_blank" rel="noopener noreferrer">epic.co.kr/home/manual/</a> · Last refreshed 2026-06-16.
            </small>
          </p>
        </section>
      </main>
    </Layout>
  );
}
