import type {ReactNode} from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';

import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <Heading as="h1" className="hero__title">
          {siteConfig.title}
        </Heading>
        <p className="hero__subtitle">{siteConfig.tagline}</p>
        <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg margin-right--md"
            to="/manuals/es-k70/intro">
            Read the ES-K70 manual
          </Link>
          <Link
            className="button button--outline button--secondary button--lg"
            to="/catalog">
            Browse all 22 manuals
          </Link>
        </div>
      </div>
    </header>
  );
}

function FeatureCard({title, body, to, cta}: {title: string; body: string; to: string; cta: string}) {
  return (
    <div className="col col--4 margin-bottom--lg">
      <div className="manual-card">
        <div>
          <h3 className="manual-card__title">{title}</h3>
          <p>{body}</p>
        </div>
        <div className="manual-card__actions">
          <Link className="button button--primary button--sm" to={to}>
            {cta}
          </Link>
        </div>
      </div>
    </div>
  );
}

export default function Home(): ReactNode {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={siteConfig.title}
      description="EPIC door-lock manuals, online. Browse all 22 official PDFs, or read the ES-K70 in full."
    >
      <HomepageHeader />
      <main className="container margin-vert--xl">
        <section className="row">
          <FeatureCard
            title="ES-K70 — full online edition"
            body="The complete ES-K70 user manual, page by page: safety, specs, components, PIN and RFID programming, deletion. Searchable, mobile-friendly, always up to date."
            to="/manuals/es-k70/intro"
            cta="Start reading →"
          />
          <FeatureCard
            title="All 22 manuals in one place"
            body="Every PDF from epic.co.kr/home/manual/ — EF, ES, N-TOUCH, POPscan, TRIPLEX, and more. Plus the consolidated manual and the EPIC Things app guide."
            to="/catalog"
            cta="Browse catalog →"
          />
          <FeatureCard
            title="Reference guides"
            body="Key-tail assembly, IR sensor wiring, outer-body cable management, and remote-control compatibility — all under /catalog."
            to="/catalog"
            cta="See references →"
          />
        </section>

        <section className="margin-top--xl">
          <Heading as="h2">About this site</Heading>
          <p>
            This is a community-built online mirror of EPIC's official manuals.
            The PDFs are unmodified copies of the documents published at{' '}
            <a href="https://www.epic.co.kr/home/manual/" target="_blank" rel="noopener noreferrer">
              epic.co.kr/home/manual/
            </a>
            . The ES-K70 has been re-typed page-by-page into web pages for easier reading and searching.
          </p>
          <p>
            For warranty, installation, and after-sales support, please contact EPIC directly:
            {' '}<a href="mailto:info@epic.co.kr">info@epic.co.kr</a>.
          </p>
        </section>
      </main>
    </Layout>
  );
}
