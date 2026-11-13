import React from 'react';
import { AbsoluteFill, Img, interpolate, staticFile, useCurrentFrame, Easing } from 'remotion';

export const TixCheckoutScene: React.FC<{ duration: number }> = ({ duration }) => {
  const frame = useCurrentFrame();

  const fadeIn = interpolate(frame, [0, 12], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  const fadeOut = interpolate(frame, [duration - 10, duration], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  // Gentle scale without covering the title
  const zoom = interpolate(frame, [0, duration], [1.0, 1.06], {
    easing: Easing.bezier(0.2, 0.8, 0.2, 1),
  });

  const badgeT = interpolate(frame, [14, 28], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: Easing.bezier(0.16, 1, 0.3, 1),
  });

  const cardT = interpolate(frame, [30, 44], [0, 1], {
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
          transform: `scale(${zoom})`,
          transformOrigin: '50% 50%',
        }}
      >
        <Img
          src={staticFile('textures/tix/video_detail.png')}
          style={{ width: 1920, height: 1080, objectFit: 'cover' }}
        />
      </div>

      {/* Floating Spotlight Card: Tour Details */}
      <div
        style={{
          position: 'absolute',
          bottom: 90,
          left: 50,
          opacity: badgeT,
          transform: `translateY(${(1 - badgeT) * 14}px)`,
          zIndex: 20,
        }}
      >
        <div
          style={{
            background: 'rgba(15, 23, 42, 0.94)',
            backdropFilter: 'blur(16px)',
            border: '1px solid rgba(255, 85, 51, 0.45)',
            borderRadius: 18,
            padding: '18px 24px',
            boxShadow: '0 20px 45px rgba(0,0,0,0.5)',
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
              Colosseo, Foro & Palatino
            </span>
          </div>
          <div style={{ color: '#ffffff', fontSize: 18, fontWeight: 800 }}>
            Slot Orari & Guide Certificate
          </div>
          <div style={{ color: '#94a3b8', fontSize: 12, marginTop: 4, lineHeight: 1.35 }}>
            Selezione lingua in tempo reale con disponibilità istantanea e prezzo in Euro.
          </div>
        </div>
      </div>

      {/* Floating Spotlight Card: Airwallex 1-Click Checkout */}
      <div
        style={{
          position: 'absolute',
          bottom: 90,
          right: 60,
          opacity: cardT,
          transform: `translateY(${(1 - cardT) * 14}px)`,
          zIndex: 20,
        }}
      >
        <div
          style={{
            background: 'rgba(15, 23, 42, 0.94)',
            backdropFilter: 'blur(16px)',
            border: '1px solid rgba(59, 130, 246, 0.5)',
            borderRadius: 18,
            padding: '20px 26px',
            boxShadow: '0 20px 45px rgba(0,0,0,0.5), 0 0 30px rgba(59, 130, 246, 0.2)',
            maxWidth: 420,
          }}
        >
          <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 6 }}>
            <span
              style={{
                width: 9,
                height: 9,
                borderRadius: '50%',
                backgroundColor: '#3b82f6',
                boxShadow: '0 0 10px #3b82f6',
              }}
            />
            <span
              style={{
                color: '#60a5fa',
                fontSize: 12,
                fontWeight: 800,
                letterSpacing: '0.14em',
                textTransform: 'uppercase',
              }}
            >
              Checkout Airwallex Integrato
            </span>
          </div>
          <div style={{ color: '#ffffff', fontSize: 18, fontWeight: 800 }}>
            Pagamenti 1-Click & Multi-Valuta
          </div>
          <div style={{ display: 'flex', gap: 8, marginTop: 10 }}>
            <div
              style={{
                background: '#ffffff',
                color: '#000000',
                padding: '6px 14px',
                borderRadius: 8,
                fontSize: 13,
                fontWeight: 800,
              }}
            >
              Apple Pay
            </div>
            <div
              style={{
                background: '#ffffff',
                color: '#000000',
                padding: '6px 14px',
                borderRadius: 8,
                fontSize: 13,
                fontWeight: 800,
              }}
            >
              Google Pay
            </div>
            <div
              style={{
                background: 'rgba(255,255,255,0.12)',
                color: '#ffffff',
                padding: '6px 14px',
                borderRadius: 8,
                fontSize: 13,
                fontWeight: 700,
              }}
            >
              EUR • USD • GBP
            </div>
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
        <span>PRENOTAZIONE ISTANTANEA · CHECKOUT ULTRA-RAPIDO IN MENO DI 30 SECONDI</span>
      </div>
    </AbsoluteFill>
  );
};
