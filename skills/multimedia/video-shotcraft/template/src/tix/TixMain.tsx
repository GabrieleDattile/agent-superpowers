import React from 'react';
import { AbsoluteFill, Audio, Sequence, staticFile } from 'remotion';
import { TixIntro } from './TixIntro';
import { TixTitleCard } from './TixTitleCard';
import { TixHeroScene } from './TixHeroScene';
import { TixMapScene } from './TixMapScene';
import { TixCheckoutScene } from './TixCheckoutScene';
import { TixHubScene } from './TixHubScene';
import { TixOperationsScene } from './TixOperationsScene';
import { TixOutro } from './TixOutro';

export const TIX_TOTAL_FRAMES = 900; // 30 seconds @ 30 fps

export const TIX_SHOTS = {
  intro: { from: 0, duration: 80 },
  hero: { from: 80, duration: 115 },
  card1: { from: 195, duration: 55 },
  map: { from: 250, duration: 120 },
  card2: { from: 370, duration: 55 },
  checkout: { from: 425, duration: 110 },
  card3: { from: 535, duration: 55 },
  hub: { from: 590, duration: 110 },
  scanner: { from: 700, duration: 110 },
  outro: { from: 810, duration: 90 },
} as const;

export const TIX_SFX = [
  // Scene 1: Intro
  { from: 0, src: 'audio/riser-cine.mp3', volume: 0.5, duration: 75 },
  { from: 30, src: 'audio/impact-cine.mp3', volume: 0.6, duration: 80 },
  { from: 48, src: 'audio/sparkle.mp3', volume: 0.35, duration: 60 },

  // Scene 2: Hero
  { from: 78, src: 'audio/whoosh-big.mp3', volume: 0.5, duration: 50 },
  { from: 110, src: 'audio/transition-soft.mp3', volume: 0.4, duration: 40 },

  // Scene 3: Card 1
  { from: 194, src: 'audio/swoosh-quick.mp3', volume: 0.45, duration: 40 },

  // Scene 4: Map
  { from: 248, src: 'audio/whoosh-fast.mp3', volume: 0.45, duration: 40 },
  { from: 275, src: 'audio/pop.mp3', volume: 0.4, duration: 30 },
  { from: 300, src: 'audio/click-camera.mp3', volume: 0.4, duration: 35 },

  // Scene 5: Card 2
  { from: 368, src: 'audio/swoosh-quick.mp3', volume: 0.45, duration: 40 },

  // Scene 6: Checkout
  { from: 424, src: 'audio/whoosh-fast.mp3', volume: 0.45, duration: 40 },
  { from: 445, src: 'audio/keyboard.mp3', volume: 0.3, duration: 30 },
  { from: 468, src: 'audio/pop.mp3', volume: 0.4, duration: 30 },

  // Scene 7: Card 3
  { from: 534, src: 'audio/swoosh-quick.mp3', volume: 0.45, duration: 40 },

  // Scene 8: Hub
  { from: 588, src: 'audio/transition-soft.mp3', volume: 0.45, duration: 40 },
  { from: 615, src: 'audio/sparkle.mp3', volume: 0.35, duration: 50 },

  // Scene 9: Scanner
  { from: 698, src: 'audio/whoosh-big.mp3', volume: 0.5, duration: 50 },
  { from: 720, src: 'audio/click-camera.mp3', volume: 0.45, duration: 35 },
  { from: 745, src: 'audio/transition-snap.mp3', volume: 0.45, duration: 35 },

  // Scene 10: Outro
  { from: 805, src: 'audio/riser-cine.mp3', volume: 0.55, duration: 80 },
  { from: 840, src: 'audio/impact-cine.mp3', volume: 0.65, duration: 85 },
  { from: 860, src: 'audio/sparkle.mp3', volume: 0.4, duration: 50 },
];

export const TixMain: React.FC = () => {
  return (
    <AbsoluteFill style={{ backgroundColor: '#070a13' }}>
      {/* SFX Audio Bed */}
      {TIX_SFX.map((sfx, idx) => (
        <Sequence
          key={`sfx-${idx}`}
          from={sfx.from}
          durationInFrames={sfx.duration}
        >
          <Audio src={staticFile(sfx.src)} volume={sfx.volume} />
        </Sequence>
      ))}

      {/* 1. Intro Brand Lockup */}
      <Sequence from={TIX_SHOTS.intro.from} durationInFrames={TIX_SHOTS.intro.duration}>
        <TixIntro duration={TIX_SHOTS.intro.duration} />
      </Sequence>

      {/* 2. Hero Scene */}
      <Sequence from={TIX_SHOTS.hero.from} durationInFrames={TIX_SHOTS.hero.duration}>
        <TixHeroScene duration={TIX_SHOTS.hero.duration} />
      </Sequence>

      {/* 3. Title Card 1: Interactive Map */}
      <Sequence from={TIX_SHOTS.card1.from} durationInFrames={TIX_SHOTS.card1.duration}>
        <TixTitleCard
          duration={TIX_SHOTS.card1.duration}
          category="NAVIGAZIONE INTUITIVA"
          words={[
            { text: 'Mappa' },
            { text: 'interattiva', accent: true },
            { text: 'e' },
            { text: 'prezzi' },
            { text: 'live' },
            { text: 'in' },
            { text: 'ogni' },
            { text: 'quartiere.' },
          ]}
          sub="OPENSTREETMAP NATIVO · ZERO WATERMARK · ZERO COSTI API"
        />
      </Sequence>

      {/* 4. Map Scene */}
      <Sequence from={TIX_SHOTS.map.from} durationInFrames={TIX_SHOTS.map.duration}>
        <TixMapScene duration={TIX_SHOTS.map.duration} />
      </Sequence>

      {/* 5. Title Card 2: 1-Click Checkout */}
      <Sequence from={TIX_SHOTS.card2.from} durationInFrames={TIX_SHOTS.card2.duration}>
        <TixTitleCard
          duration={TIX_SHOTS.card2.duration}
          category="CHECKOUT AIRWALLEX"
          words={[
            { text: 'Esperienze' },
            { text: 'uniche' },
            { text: 'con' },
            { text: 'prenotazione' },
            { text: '1-Click', accent: true },
            { text: 'immediata.' },
          ]}
          sub="APPLE PAY · GOOGLE PAY · MULTI-VALUTA IN TEMPO REALE"
        />
      </Sequence>

      {/* 6. Checkout Scene */}
      <Sequence from={TIX_SHOTS.checkout.from} durationInFrames={TIX_SHOTS.checkout.duration}>
        <TixCheckoutScene duration={TIX_SHOTS.checkout.duration} />
      </Sequence>

      {/* 7. Title Card 3: Day-of-Tour Hub */}
      <Sequence from={TIX_SHOTS.card3.from} durationInFrames={TIX_SHOTS.card3.duration}>
        <TixTitleCard
          duration={TIX_SHOTS.card3.duration}
          category="ESPERIENZA SENZA PENSIERI"
          words={[
            { text: 'Il' },
            { text: 'giorno' },
            { text: 'del' },
            { text: 'tour:' },
            { text: 'zero', accent: true },
            { text: 'stress,' },
            { text: 'tutto' },
            { text: 'offline.' },
          ]}
          sub="COUNTDOWN DINAMICO · METEO DESTINAZIONE · CHECKLIST PRE-PARTENZA"
        />
      </Sequence>

      {/* 8. Day-of-Tour Hub Scene */}
      <Sequence from={TIX_SHOTS.hub.from} durationInFrames={TIX_SHOTS.hub.duration}>
        <TixHubScene duration={TIX_SHOTS.hub.duration} />
      </Sequence>

      {/* 9. Field Operations Scanner & Manifest Scene */}
      <Sequence from={TIX_SHOTS.scanner.from} durationInFrames={TIX_SHOTS.scanner.duration}>
        <TixOperationsScene duration={TIX_SHOTS.scanner.duration} />
      </Sequence>

      {/* 10. Outro Finale */}
      <Sequence from={TIX_SHOTS.outro.from} durationInFrames={TIX_SHOTS.outro.duration}>
        <TixOutro duration={TIX_SHOTS.outro.duration} />
      </Sequence>
    </AbsoluteFill>
  );
};
