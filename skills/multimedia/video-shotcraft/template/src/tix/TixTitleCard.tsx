import React from 'react';
import { AbsoluteFill, interpolate, useCurrentFrame, Easing } from 'remotion';

export interface TixTitleCardProps {
  duration: number;
  words: { text: string; accent?: boolean }[];
  sub?: string;
  category?: string;
}

export const TixTitleCard: React.FC<TixTitleCardProps> = ({
  duration,
  words,
  sub,
  category = 'TIX E TOURS',
}) => {
  const frame = useCurrentFrame();

  const fadeOut = interpolate(frame, [duration - 8, duration], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  const underline = interpolate(frame, [8, 22], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: Easing.bezier(0.3, 0, 0.2, 1),
  });

  const catT = interpolate(frame, [0, 12], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  const subT = interpolate(frame, [14, 26], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  return (
    <AbsoluteFill
      style={{
        backgroundColor: '#0a0f1d',
        justifyContent: 'center',
        alignItems: 'center',
        opacity: fadeOut,
        backgroundImage:
          'radial-gradient(1200px 800px at 50% 45%, rgba(255, 85, 51, 0.12), transparent 70%), radial-gradient(800px 500px at 50% 50%, rgba(26, 42, 68, 0.7), transparent 80%)',
      }}
    >
      <div style={{ textAlign: 'center', maxWidth: 1400, padding: '0 40px' }}>
        {/* Category Pill */}
        <div
          style={{
            display: 'inline-flex',
            alignItems: 'center',
            gap: 8,
            padding: '8px 20px',
            borderRadius: 999,
            background: 'rgba(255, 85, 51, 0.15)',
            border: '1px solid rgba(255, 85, 51, 0.35)',
            color: '#ff7755',
            fontFamily: 'Inter, system-ui, -apple-system, sans-serif',
            fontSize: 18,
            fontWeight: 800,
            letterSpacing: '0.18em',
            textTransform: 'uppercase',
            marginBottom: 24,
            opacity: catT,
            transform: `translateY(${(1 - catT) * 10}px)`,
          }}
        >
          <span
            style={{
              width: 8,
              height: 8,
              borderRadius: '50%',
              backgroundColor: '#ff5533',
              boxShadow: '0 0 10px #ff5533',
            }}
          />
          {category}
        </div>

        {/* Main Headline with tight, complete reveal */}
        <div
          style={{
            fontFamily: 'Inter, system-ui, -apple-system, sans-serif',
            fontSize: 76,
            fontWeight: 900,
            lineHeight: 1.15,
            color: '#ffffff',
            letterSpacing: '-0.025em',
            display: 'flex',
            flexWrap: 'wrap',
            justifyContent: 'center',
            columnGap: '0.28em',
          }}
        >
          {words.map((w, i) => {
            const delay = 1 + i * 2.2;
            const t = interpolate(frame, [delay, delay + 7], [0, 1], {
              extrapolateLeft: 'clamp',
              extrapolateRight: 'clamp',
              easing: Easing.bezier(0.2, 0.75, 0.3, 1),
            });
            return (
              <span
                key={i}
                style={{
                  opacity: t,
                  transform: `scale(${1.15 - 0.15 * t})`,
                  filter: `blur(${(1 - t) * 5}px)`,
                  display: 'inline-block',
                  color: w.accent ? '#ff5533' : '#ffffff',
                  textShadow: w.accent
                    ? '0 0 40px rgba(255, 85, 51, 0.5)'
                    : '0 2px 20px rgba(0,0,0,0.4)',
                }}
              >
                {w.text}
              </span>
            );
          })}
        </div>

        {/* Glowing Underline Accent */}
        <div
          style={{
            height: 5,
            width: 240,
            margin: '30px auto 0',
            borderRadius: 4,
            background: 'linear-gradient(90deg, #ff5533, #ff8844)',
            boxShadow: '0 0 20px rgba(255, 85, 51, 0.7)',
            transform: `scaleX(${underline})`,
          }}
        />

        {/* Subtitle */}
        {sub ? (
          <div
            style={{
              fontFamily: 'Inter, system-ui, -apple-system, sans-serif',
              fontSize: 24,
              fontWeight: 600,
              letterSpacing: '0.12em',
              color: '#94a3b8',
              marginTop: 26,
              opacity: subT,
              textTransform: 'uppercase',
            }}
          >
            {sub}
          </div>
        ) : null}
      </div>
    </AbsoluteFill>
  );
};
