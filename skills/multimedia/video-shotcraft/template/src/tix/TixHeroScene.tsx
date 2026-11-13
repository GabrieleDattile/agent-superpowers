import React from 'react';
import { AbsoluteFill, Img, interpolate, staticFile, useCurrentFrame, Easing } from 'remotion';

export const TixHeroScene: React.FC<{ duration: number }> = ({ duration }) => {
  const frame = useCurrentFrame();

  // Very gentle camera breathing: keeps the top navbar fully visible
  const zoom = interpolate(frame, [0, duration], [1.0, 1.05], {
    easing: Easing.bezier(0.25, 0.1, 0.25, 1),
  });

  const fadeIn = interpolate(frame, [0, 12], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  const fadeOut = interpolate(frame, [duration - 10, duration], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  // Floating highlight callout card
  const calloutT = interpolate(frame, [16, 30], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: Easing.bezier(0.16, 1, 0.3, 1),
  });

  return (
    <AbsoluteFill
      style={{
        backgroundColor: '#0a0f1d',
        overflow: 'hidden',
        opacity: fadeIn * fadeOut,
      }}
    >
      {/* Page Screenshot with intact navbar */}
      <div
        style={{
          width: '100%',
          height: '100%',
          transform: `scale(${zoom})`,
          transformOrigin: '50% 45%',
        }}
      >
        <Img
          src={staticFile('textures/tix/video_hero.png')}
          style={{ width: 1920, height: 1080, objectFit: 'cover' }}
        />
      </div>

      {/* Floating 3D Highlight Card */}
      <div
        style={{
          position: 'absolute',
          top: 105,
          right: 70,
          opacity: calloutT,
          transform: `translateY(${(1 - calloutT) * 16}px)`,
          zIndex: 20,
        }}
      >
        <div
          style={{
            background: 'rgba(15, 23, 42, 0.92)',
            backdropFilter: 'blur(16px)',
            border: '1px solid rgba(255, 85, 51, 0.4)',
            borderRadius: 18,
            padding: '20px 24px',
            boxShadow: '0 20px 45px rgba(0,0,0,0.5), 0 0 30px rgba(255, 85, 51, 0.2)',
            display: 'flex',
            flexDirection: 'column',
            gap: 8,
            maxWidth: 360,
          }}
        >
          <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
            <span
              style={{
                width: 10,
                height: 10,
                borderRadius: '50%',
                backgroundColor: '#ff5533',
                boxShadow: '0 0 12px #ff5533',
              }}
            />
            <span
              style={{
                color: '#ff7755',
                fontSize: 13,
                fontWeight: 800,
                letterSpacing: '0.15em',
                textTransform: 'uppercase',
              }}
            >
              Colosseo al Tramonto
            </span>
          </div>

          <div
            style={{
              color: '#ffffff',
              fontSize: 19,
              fontWeight: 800,
              lineHeight: 1.25,
            }}
          >
            Nuovo Sfondo Panoramico & Brand Tix e Tours
          </div>

          <div
            style={{
              color: '#94a3b8',
              fontSize: 13,
              lineHeight: 1.35,
            }}
          >
            Fotografia d'autore in alta risoluzione, switch rapido città e ricerca istantanea.
          </div>
        </div>
      </div>

      {/* Bottom Cinematic Caption */}
      <div
        style={{
          position: 'absolute',
          bottom: 30,
          left: '50%',
          transform: 'translateX(-50%)',
          background: 'rgba(11, 17, 32, 0.94)',
          border: '1px solid rgba(255, 255, 255, 0.15)',
          borderRadius: 12,
          padding: '10px 26px',
          display: 'flex',
          alignItems: 'center',
          gap: 12,
          color: '#ffffff',
          fontFamily: 'Inter, system-ui, -apple-system, sans-serif',
          fontSize: 17,
          fontWeight: 700,
          letterSpacing: '0.14em',
          textTransform: 'uppercase',
          boxShadow: '0 10px 30px rgba(0,0,0,0.5)',
        }}
      >
        <span style={{ width: 8, height: 8, borderRadius: 2, backgroundColor: '#ff5533' }} />
        <span>TIX E TOURS · OLTRE 150 DESTINAZIONI GLOBALI</span>
      </div>
    </AbsoluteFill>
  );
};
