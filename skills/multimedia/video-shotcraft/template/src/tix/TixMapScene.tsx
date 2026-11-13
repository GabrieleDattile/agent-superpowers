import React from 'react';
import { AbsoluteFill, Img, interpolate, staticFile, useCurrentFrame, Easing } from 'remotion';

export const TixMapScene: React.FC<{ duration: number }> = ({ duration }) => {
  const frame = useCurrentFrame();

  // Gentle push-in towards the map area without cutting off the title
  const zoom = interpolate(frame, [0, duration], [1.0, 1.08], {
    easing: Easing.bezier(0.2, 0.8, 0.2, 1),
  });

  const panX = interpolate(frame, [0, duration], [0, -60], {
    easing: Easing.bezier(0.2, 0.8, 0.2, 1),
  });

  const fadeIn = interpolate(frame, [0, 12], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  const fadeOut = interpolate(frame, [duration - 10, duration], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  const pin1T = interpolate(frame, [14, 28], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: Easing.bezier(0.16, 1, 0.3, 1),
  });

  const pin2T = interpolate(frame, [30, 44], [0, 1], {
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
          transform: `scale(${zoom}) translateX(${panX}px)`,
          transformOrigin: '65% 50%',
        }}
      >
        <Img
          src={staticFile('textures/tix/video_search.png')}
          style={{ width: 1920, height: 1080, objectFit: 'cover' }}
        />
      </div>

      {/* Floating Spotlight Badge 1: OpenStreetMap Tile Provider */}
      <div
        style={{
          position: 'absolute',
          top: 140,
          left: 50,
          opacity: pin1T,
          transform: `translateY(${(1 - pin1T) * 14}px)`,
          zIndex: 20,
        }}
      >
        <div
          style={{
            background: 'rgba(15, 23, 42, 0.94)',
            backdropFilter: 'blur(14px)',
            border: '1px solid rgba(16, 185, 129, 0.45)',
            borderRadius: 16,
            padding: '16px 22px',
            boxShadow: '0 20px 40px rgba(0,0,0,0.5)',
            maxWidth: 360,
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
                letterSpacing: '0.12em',
                textTransform: 'uppercase',
              }}
            >
              OpenStreetMap Nativo
            </span>
          </div>
          <div style={{ color: '#ffffff', fontSize: 17, fontWeight: 800 }}>
            Zero Watermark & Zero Costi API
          </div>
          <div style={{ color: '#94a3b8', fontSize: 12, marginTop: 4, lineHeight: 1.35 }}>
            Tile server ad alte prestazioni senza costi di licenza o limitazioni di traffico.
          </div>
        </div>
      </div>

      {/* Floating Spotlight Badge 2: Dynamic Live Price Pins */}
      <div
        style={{
          position: 'absolute',
          bottom: 90,
          right: 70,
          opacity: pin2T,
          transform: `translateY(${(1 - pin2T) * 14}px)`,
          zIndex: 20,
        }}
      >
        <div
          style={{
            background: 'rgba(15, 23, 42, 0.94)',
            backdropFilter: 'blur(14px)',
            border: '1px solid rgba(255, 85, 51, 0.5)',
            borderRadius: 16,
            padding: '16px 22px',
            boxShadow: '0 20px 40px rgba(0,0,0,0.5), 0 0 25px rgba(255, 85, 51, 0.25)',
            maxWidth: 360,
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
                letterSpacing: '0.12em',
                textTransform: 'uppercase',
              }}
            >
              Pin Dinamici a Roma
            </span>
          </div>
          <div style={{ color: '#ffffff', fontSize: 17, fontWeight: 800 }}>
            Prezzi Live Sincronizzati
          </div>
          <div style={{ color: '#94a3b8', fontSize: 12, marginTop: 4, lineHeight: 1.35 }}>
            Vaticano €69, Trastevere €52, Colosseo €48: aggiornamento istantaneo con i filtri.
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
        <span>MAPPA INTERATTIVA A ROMA · PREZZI LIVE IN TUTTI I QUARTIERI</span>
      </div>
    </AbsoluteFill>
  );
};
