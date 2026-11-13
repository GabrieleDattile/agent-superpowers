import React from 'react';
import { AbsoluteFill, interpolate, useCurrentFrame, Easing } from 'remotion';

export const TixOutro: React.FC<{ duration: number }> = ({ duration }) => {
  const frame = useCurrentFrame();

  const scale = interpolate(frame, [0, 45], [0.88, 1], {
    easing: Easing.bezier(0.16, 1, 0.3, 1),
  });

  const opacity = interpolate(frame, [0, 20], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  const ctaT = interpolate(frame, [25, 45], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: Easing.bezier(0.16, 1, 0.3, 1),
  });

  const sparkleGlow = interpolate(frame, [45, 65, 85], [0.3, 0.8, 0.5], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  return (
    <AbsoluteFill
      style={{
        backgroundColor: '#070a13',
        justifyContent: 'center',
        alignItems: 'center',
        overflow: 'hidden',
        opacity,
      }}
    >
      {/* Background radial glow */}
      <div
        style={{
          position: 'absolute',
          width: 1300,
          height: 1300,
          borderRadius: '50%',
          background: 'radial-gradient(circle, rgba(255, 85, 51, 0.22) 0%, rgba(13, 20, 35, 0.6) 45%, transparent 70%)',
          filter: 'blur(70px)',
          opacity: sparkleGlow,
        }}
      />

      <div
        style={{
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          textAlign: 'center',
          transform: `scale(${scale})`,
          zIndex: 10,
        }}
      >
        {/* Brand Lockup */}
        <div style={{ display: 'flex', alignItems: 'center', gap: 24, marginBottom: 20 }}>
          <div
            style={{
              width: 96,
              height: 96,
              borderRadius: 28,
              background: 'linear-gradient(135deg, #ff5533, #e6391a)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              boxShadow: '0 16px 40px rgba(255, 85, 51, 0.5)',
            }}
          >
            <svg
              width="58"
              height="58"
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
                fontSize: 90,
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
                fontSize: 18,
                fontWeight: 800,
                letterSpacing: '0.3em',
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
            fontSize: 42,
            fontWeight: 700,
            color: '#e2e8f0',
            letterSpacing: '-0.02em',
            marginTop: 18,
          }}
        >
          Rendi ogni viaggio <span style={{ color: '#ff5533' }}>indimenticabile.</span>
        </div>

        {/* CTA Button */}
        <div
          style={{
            marginTop: 44,
            opacity: ctaT,
            transform: `translateY(${(1 - ctaT) * 16}px)`,
          }}
        >
          <div
            style={{
              padding: '18px 48px',
              borderRadius: 16,
              background: 'linear-gradient(135deg, #ff5533, #e6391a)',
              color: '#ffffff',
              fontSize: 24,
              fontWeight: 800,
              letterSpacing: '0.04em',
              boxShadow: '0 15px 40px rgba(255, 85, 51, 0.45)',
              display: 'inline-flex',
              alignItems: 'center',
              gap: 14,
            }}
          >
            <span>Esplora la Piattaforma</span>
            <span style={{ fontSize: 26 }}>→</span>
          </div>
        </div>

        {/* Domain footer */}
        <div
          style={{
            marginTop: 28,
            color: '#94a3b8',
            fontFamily: 'monospace',
            fontSize: 18,
            letterSpacing: '0.12em',
            opacity: ctaT,
          }}
        >
          TIXETOURS.COM · DISPONIBILE ORA
        </div>
      </div>
    </AbsoluteFill>
  );
};
