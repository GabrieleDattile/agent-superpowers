import React from 'react';
import { AbsoluteFill, Img, interpolate, staticFile, useCurrentFrame, Easing } from 'remotion';

export const TixHubScene: React.FC<{ duration: number }> = ({ duration }) => {
  const frame = useCurrentFrame();

  const fadeIn = interpolate(frame, [0, 12], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  const fadeOut = interpolate(frame, [duration - 10, duration], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  // Camera focuses on the Hub
  const zoom = interpolate(frame, [0, duration], [1.0, 1.08], {
    easing: Easing.bezier(0.2, 0.8, 0.2, 1),
  });

  const panY = interpolate(frame, [0, duration], [0, -110], {
    easing: Easing.bezier(0.2, 0.8, 0.2, 1),
  });

  const feat1T = interpolate(frame, [14, 28], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: Easing.bezier(0.16, 1, 0.3, 1),
  });

  const feat2T = interpolate(frame, [30, 44], [0, 1], {
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
      <div
        style={{
          width: '100%',
          height: '100%',
          transform: `scale(${zoom}) translateY(${panY}px)`,
          transformOrigin: '50% 35%',
        }}
      >
        <Img
          src={staticFile('textures/tix/video_voucher.png')}
          style={{ width: 1920, height: 1080, objectFit: 'cover' }}
        />
      </div>

      {/* Feature Card 1: Countdown & Weather Simulator */}
      <div
        style={{
          position: 'absolute',
          top: 90,
          left: 50,
          opacity: feat1T,
          transform: `translateY(${(1 - feat1T) * 14}px)`,
          zIndex: 20,
        }}
      >
        <div
          style={{
            background: 'rgba(15, 23, 42, 0.94)',
            backdropFilter: 'blur(16px)',
            border: '1px solid rgba(255, 85, 51, 0.5)',
            borderRadius: 18,
            padding: '18px 24px',
            boxShadow: '0 20px 45px rgba(0,0,0,0.5), 0 0 25px rgba(255, 85, 51, 0.25)',
            maxWidth: 380,
          }}
        >
          <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 6 }}>
            <span
              style={{
                width: 9,
                height: 9,
                borderRadius: '50%',
                backgroundColor: '#ff5533',
                boxShadow: '0 0 10px #ff5533',
              }}
            />
            <span
              style={{
                color: '#ff7755',
                fontSize: 12,
                fontWeight: 800,
                letterSpacing: '0.14em',
                textTransform: 'uppercase',
              }}
            >
              Widget Il Giorno del Tour
            </span>
          </div>
          <div style={{ color: '#ffffff', fontSize: 18, fontWeight: 800 }}>
            Countdown Live & Meteo Roma
          </div>
          <div style={{ display: 'flex', flexDirection: 'column', gap: 4, marginTop: 8 }}>
            <div style={{ color: '#fbbf24', fontSize: 13, fontWeight: 700 }}>
              ⏱ Conto alla rovescia dinamico in tempo reale
            </div>
            <div style={{ color: '#38bdf8', fontSize: 13, fontWeight: 700 }}>
              ☀️ Roma: 22°C Soleggiato · Clima Ideale
            </div>
          </div>
        </div>
      </div>

      {/* Feature Card 2: Interactive Checklist & PDF Pass */}
      <div
        style={{
          position: 'absolute',
          bottom: 90,
          right: 60,
          opacity: feat2T,
          transform: `translateY(${(1 - feat2T) * 14}px)`,
          zIndex: 20,
        }}
      >
        <div
          style={{
            background: 'rgba(15, 23, 42, 0.94)',
            backdropFilter: 'blur(16px)',
            border: '1px solid rgba(16, 185, 129, 0.5)',
            borderRadius: 18,
            padding: '18px 24px',
            boxShadow: '0 20px 45px rgba(0,0,0,0.5), 0 0 25px rgba(16, 185, 129, 0.2)',
            maxWidth: 400,
          }}
        >
          <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 6 }}>
            <span
              style={{
                width: 9,
                height: 9,
                borderRadius: '50%',
                backgroundColor: '#10b981',
                boxShadow: '0 0 10px #10b981',
              }}
            />
            <span
              style={{
                color: '#34d399',
                fontSize: 12,
                fontWeight: 800,
                letterSpacing: '0.14em',
                textTransform: 'uppercase',
              }}
            >
              Pass d'Imbarco Ufficiale (PDF)
            </span>
          </div>
          <div style={{ color: '#ffffff', fontSize: 18, fontWeight: 800 }}>
            Massima Comodità Offline
          </div>
          <div style={{ color: '#94a3b8', fontSize: 12, marginTop: 6, lineHeight: 1.35 }}>
            Layout boarding-pass con QR vettoriale, coordinate GPS e note di conformità per Colosseo e Musei Vaticani.
          </div>
        </div>
      </div>

      {/* Bottom Cinematic Caption */}
      <div
        style={{
          position: 'absolute',
          bottom: 18,
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
        <span>TUTTO IL GIORNO DEL TOUR IN UN TOCCO · 100% OFFLINE READY</span>
      </div>
    </AbsoluteFill>
  );
};
