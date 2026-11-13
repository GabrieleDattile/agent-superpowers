import { Composition } from 'remotion';
import { AIFL_TOTAL } from './aifl/Main';
import { ThemedFilm } from './themes/ThemedFilm';
import { TixMain, TIX_TOTAL_FRAMES } from './tix/TixMain';

export const Root: React.FC = () => {
  return (
    <>
      <Composition
        id="TixEToursPromo"
        component={TixMain}
        durationInFrames={TIX_TOTAL_FRAMES}
        fps={30}
        width={1920}
        height={1080}
      />
      <Composition
        id="AiflPromo"
        component={ThemedFilm}
        defaultProps={{theme: 'ink-press'}}
        durationInFrames={AIFL_TOTAL}
        fps={30}
        width={1920}
        height={1080}
      />
    </>
  );
};
