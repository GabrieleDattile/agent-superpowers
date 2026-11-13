import React from 'react';
import { AbsoluteFill, interpolate, useCurrentFrame, Easing } from 'remotion';

export const TixIntro: React.FC<{ duration: number }> = ({ duration }) => {
  const frame = useCurrentFrame();

  const logoScale = interpolate(frame, [0, 36], [0.88, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: Easing.bezier(0.16, 1, 0.3, 1),
  });

  const logoOpacity = interpolate(frame, [0, 20], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  const compassRot = interpolate(frame, [0, 60], [-45, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: Easing.bezier(0.16, 1, 0.3, 1),
  });

  const taglineT = interpolate(frame, [22, 40], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: Easing.bezier(0.16, 1, 0.3, 1),
  });

  const badgesT = interpolate(frame, [40, 58], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  const fadeOut = interpolate(frame, [duration - 10, duration], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  return (
    <AbsoluteFill
      style={{
        backgroundColor: '#070a13',
        justifyContent: 'center',
        alignItems: 'center',
        opacity: fadeOut,
        overflow: 'hidden',
      }}
    >
      {/* Background ambient radial gradients */}
      <div
        style={{
          position: 'absolute',
          width: 1300,
          height: 1300,
          borderRadius: '50%',
          background: 'radial-gradient(circle, rgba(255, 85, 51, 0.2) 0%, rgba(13, 20, 35, 0.6) 45%, transparent 70%)',
          filter: 'blur(60px)',
          transform: `scale(${1 + Math.sin(frame / 20) * 0.04})`,
        }}
      />

      <div
        style={{
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          textAlign: 'center',
          transform: `scale(${logoScale})`,
          opacity: logoOpacity,
          zIndex: 10,
        }}
      >
        {/* Brand Lockup: Compass Icon + Tix e Tours */}
        <div style={{ display: 'flex', alignItems: 'center', gap: 22, marginBottom: 18 }}>
          <div
            style={{
              width: 88,
              height: 88,
              borderRadius: 26,
              background: 'linear-gradient(135deg, #ff5533, #e6391a)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              boxShadow: '0 12px 35px rgba(255, 85, 51, 0.45)',
              transform: `rotate(${compassRot}deg)`,
            }}
          >
            <svg
              width="52"
              height="52"
              viewBox="0 0 24 24"
              fill="none"
              stroke="#ffffff"
              strokeWidth="2.2"
              strokeLinecap="round"
              strokeLinejoin="round"
            >
              <circle cx="12" cy="12" r="10" />
              <polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76" fill="#ffffff" fillOpacity="0.25" />
            </svg>
          </div>

          <div style={{ textAlign: 'left' }}>
            <div
              style={{
                fontFamily: 'Inter, system-ui, -apple-system, sans-serif',
                fontSize: 82,
                fontWeight: 900,
                color: '#ffffff',
                letterSpacing: '-0.035em',
                lineHeight: 1,
              }}
            >
              Tix e Tours
            </div>
            <div
              style={{
                fontFamily: 'Inter, system-ui, -apple-system, sans-serif',
                fontSize: 16,
                fontWeight: 800,
                letterSpacing: '0.28em',
                color: '#ff7755',
                textTransform: 'uppercase',
                marginTop: 6,
              }}
            >
              Originals & Curated Experiences
            </div>
          </div>
        </div>

        {/* Tagline */}
        <div
          style={{
            fontFamily: 'Inter, system-ui, -apple-system, sans-serif',
            fontSize: 38,
            fontWeight: 700,
            color: '#e2e8f0',
            letterSpacing: '-0.015em',
            marginTop: 14,
            opacity: taglineT,
            transform: `translateY(${(1 - taglineT) * 14}px)`,
          }}
        >
          Rendi ogni viaggio <span style={{ color: '#ff5533' }}>indimenticabile.</span>
        </div>

        {/* Dynamic Pillar Badges */}
        <div
          style={{
            display: 'flex',
            gap: 16,
            marginTop: 36,
            opacity: badgesT,
            transform: `translateY(${(1 - badgesT) * 14}px)`,
          }}
        >
          {[
            'Mappa Interattiva Senza Costi API',
            'Pass d\'Imbarco Offline & Countdown Hub',
            'Scanner Guide & Manifesto Passeggeri',
          ].map((tag, idx) => (
            <div
              key={idx}
              style={{
                padding: '9px 20px',
                borderRadius: 999,
                background: 'rgba(255, 255, 255, 0.08)',
                backdropFilter: 'blur(10px)',
                border: '1px solid rgba(255, 255, 255, 0.14)',
                color: '#cbd5e1',
                fontSize: 15,
                fontWeight: 600,
                letterSpacing: '0.04em',
              }}
            >
              ✦ {tag}
            </div>
          ))}
        </div>
      </div>
    </AbsoluteFill>
  );
};
